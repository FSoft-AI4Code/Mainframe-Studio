import uuid
import pika
from loguru import logger
from app.config.settings import settings
import time
from functools import wraps


def retry_operation(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (pika.exceptions.AMQPConnectionError,
                        pika.exceptions.ChannelClosedByBroker,
                        pika.exceptions.ChannelWrongStateError) as e:
                    logger.warning(f"RabbitMQ operation failed: {str(e)}. Retry {retries + 1}/{max_retries}")
                    retries += 1
                    if retries < max_retries:
                        time.sleep(delay)
                    else:
                        raise

        return wrapper

    return decorator


class RabbitHelper:
    def __init__(self, exchange: str, queue_name: str, routing_key: str,
                 enable_consume: bool = False, dlx_queue: bool = False):
        self.exchange = exchange
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.enable_consume = enable_consume
        self.dlx_queue = dlx_queue
        self.response = None
        self.corr_id = None

        # Create a new connection for each instance
        self._create_connection()
        self._setup_channel()

    def _create_connection(self):
        """Create a new connection with heartbeat and retry while broker starts"""
        parameters = pika.URLParameters(settings.RABBITMQ_URL)
        parameters.heartbeat = 30  # 30 seconds heartbeat
        parameters.blocked_connection_timeout = 30

        max_attempts = 10
        delay_seconds = 2
        attempt = 0
        last_error = None
        while attempt < max_attempts:
            try:
                self.connection = pika.BlockingConnection(parameters)
                return
            except pika.exceptions.AMQPConnectionError as e:
                last_error = e
                logger.warning(
                    f"RabbitMQ not ready yet (attempt {attempt + 1}/{max_attempts}): {str(e)}"
                )
                time.sleep(delay_seconds)
                attempt += 1

        # If we get here, all attempts failed
        logger.error(f"Failed to connect to RabbitMQ after {max_attempts} attempts: {str(last_error)}")
        raise last_error

    def _setup_channel(self):
        """Setup the channel with exchanges and queues"""
        self.channel = self.connection.channel()

        # Declare exchange
        self.channel.exchange_declare(
            exchange=self.exchange,
            exchange_type='topic',
            durable=True
        )

        args = {
            "x-dead-letter-exchange": self.exchange,
            "x-dead-letter-routing-key": self.routing_key
        } if self.dlx_queue else {}

        try:
            self.channel.queue_declare(queue=self.queue_name, passive=True)
        except pika.exceptions.ChannelClosedByBroker:
            logger.warning(f"Queue '{self.queue_name}' does not exist. Creating it.")
            # Reopen the channel after it gets closed
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name, durable=True, arguments=args)
            self.channel.queue_bind(
                queue=self.queue_name,
                exchange=self.exchange,
                routing_key=self.routing_key
            )

        if self.enable_consume:
            self.channel.basic_consume(
                queue=self.queue_name,
                on_message_callback=self.on_response,
                auto_ack=True
            )

    def on_response(self, ch, method, props, body):
        logger.info(f"Received message with props correlation_id: {props.correlation_id}")
        if self.corr_id == props.correlation_id:
            self.response = body

    def _ensure_connection(self):
        """Ensure the connection and channel are open"""
        try:
            if not self.connection or self.connection.is_closed:
                logger.info("Reconnecting to RabbitMQ...")
                self._create_connection()
                self._setup_channel()
            elif not self.channel or self.channel.is_closed:
                logger.info("Recreating channel...")
                self._setup_channel()
        except Exception as e:
            logger.error(f"Failed to ensure connection: {str(e)}")
            raise

    @retry_operation(max_retries=3, delay=2)
    def call(self, exchange: str, routing_key: str, body: str, properties: pika.BasicProperties,
             wait_response: bool = False):
        self._ensure_connection()
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            properties=properties,
            body=body
        )

        if wait_response:
            timeout = 300  # 5 minutes timeout
            start_time = time.time()
            while self.response is None:
                if time.time() - start_time > timeout:
                    raise TimeoutError(f"No response received after {timeout} seconds")
                self.connection.process_data_events(time_limit=1)
            return self.response