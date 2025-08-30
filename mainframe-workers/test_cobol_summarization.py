import json
import pika
import traceback
from src.config.settings import settings

def send_test_message():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=pika.PlainCredentials(
                settings.RABBITMQ_USER, 
                settings.RABBITMQ_PASSWORD
            )
        )
    )
    
    channel = connection.channel()
    
    # Get queue config
    queue_config = settings.QUEUE_CONFIGS["cobol_summarization"]
    queue_name = settings.COBOL_SUMMARIZATION_QUEUE_NAME
    exchange = settings.PARSER_EXCHANGE_NAME
    routing_key = settings.COBOL_SUMMARIZATION_ROUTING_KEY  
    
    # Declare the queue
    channel.queue_declare(queue=queue_name, durable=True)
    
    # If using an exchange, declare it
    if exchange:
        channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)
        channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)
    
    # Test message
    test_message = {
        "task_type": "summarize_cobol",
        "data": {
            "name": "ZRIH0005_SJ",
            "repository_id": "6789d7244d6f024452cfb2c5",
        }
    }
    
    # Send message with exchange and routing key
    channel.basic_publish(
        exchange=exchange,
        routing_key=routing_key,
        body=json.dumps(test_message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    
    print(f" [x] Sent test message: {test_message}")
    
    connection.close()

if __name__ == "__main__":
    try:
        send_test_message()
        print(" [*] Test message sent successfully")
    except Exception as e:
        print(f" [!] Error sending test message: {str(e)}")
        print("Traceback:")
        print(traceback.format_exc())