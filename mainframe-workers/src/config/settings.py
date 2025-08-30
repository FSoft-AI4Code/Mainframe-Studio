from typing import Dict

from loguru import logger
from pydantic_settings import BaseSettings
from pydantic import field_validator


class QueueConfig:

    def __init__(
        self,
        name: str,
        exchange: str,
        routing_key: str,
        requeue_delay_time_in_seconds: int = 0,
    ):
        self.name = name
        self.exchange = exchange
        self.routing_key = routing_key
        self.requeue_delay_time_in_seconds = requeue_delay_time_in_seconds


class Settings(BaseSettings):
    # RabbitMQ settings
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"
    RABBITMQ_VHOST: str = "/"
    RABBITMQ_HEARTBEAT: int = 3000

    # Azure Storage settings
    AZURE_STORAGE_CONNECTION_STRING: str
    AZURE_STORAGE_CONTAINER_NAME: str
    AZURE_STORAGE_URL: str

    # Azure OpenAI settings
    AZURE_OPENAI_API_BASE: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_MODEL: str
    AZURE_OPENAI_MODEL_TYPE: str
    AZURE_OPENAI_API_VERSION: str
    LLM_PROVIDER: str

    # Assistant Agent Settings
    ASSISTANT_AGENT_TEMPERATURE: float = 0.0
    ASSISTANT_AGENT_TOP_P: float = 1.0
    ASSISTANT_AGENT_FREQUENCY_PENALTY: float = 0.0
    ASSISTANT_AGENT_PRESENCE_PENALTY: float = 0.0

    # Parser settings
    COBOL_PARSER_TIME_LIMIT_IN_SECONDS: int = 3000

    @field_validator("COBOL_PARSER_TIME_LIMIT_IN_SECONDS")
    def validate_cobol_parser_time_limit(cls, v, values):
        if "RABBITMQ_HEARTBEAT" in values.data and v > values.data["RABBITMQ_HEARTBEAT"]:
            logger.error(
                "COBOL_PARSER_TIME_LIMIT_IN_SECONDS must be less than or equal to RABBITMQ_HEARTBEAT",
                cobol_parser_time_limit=v,
                rabbitmq_heartbeat=values.data["RABBITMQ_HEARTBEAT"],
            )
            raise ValueError()
        return v

    # Worker settings
    WORKER_PREFETCH_COUNT: int = 1

    # Queue Names
    EMAIL_QUEUE_NAME: str = "email_queue"
    NOTIFICATION_QUEUE_NAME: str = "notification_queue"
    PROCESSING_QUEUE_NAME: str = "processing_queue"
    COPYBOOK_DNP_QUEUE_NAME: str = "copybook_dnp_queue"
    COPYBOOK_UNISYS_QUEUE_NAME: str = "copybook_unisys_queue"
    PANEL_QUEUE_NAME: str = "panel_queue"
    PANEL_DISPATCHER_QUEUE_NAME: str = "panel_dispatcher_queue"
    REPORT_QUEUE_NAME: str = "report_queue"
    REPORT_DISPATCHER_QUEUE_NAME: str = "report_dispatcher_queue"
    CLIST_QUEUE_NAME: str = "clist_queue"
    CLIST_DISPATCHER_QUEUE_NAME: str = "clist_dispatcher_queue"
    PANEL_QUEUE_NAME: str = "panel_queue"
    PANEL_DISPATCHER_QUEUE_NAME: str = "panel_dispatcher_queue"
    REPORT_QUEUE_NAME: str = "report_queue"
    REPORT_DISPATCHER_QUEUE_NAME: str = "report_dispatcher_queue"
    BMS_SUMMARIZATION_QUEUE_NAME: str = "bms_summarization_queue"
    COBOL_SCREEN_SUMMARIZATION_QUEUE_NAME: str = "coboL_screen_summarization_queue"
    COBOL_JAVA_MIGRATION_QUEUE_NAME: str = "coboL_java_migration_queue"
    BMS_JAVA_MIGRATION_QUEUE_NAME: str = "bms_java_migration_queue"
    BAT_QUEUE_NAME: str = "bat_queue"
    COBOL_DISPATCHER_QUEUE_NAME: str = "cobol_dispatcher_queue"
    WFL_DISPATCHER_QUEUE_NAME: str = "wfl_dispatcher_queue"
    SCREEN_ACCESS_QUEUE_NAME: str = "screen_access_queue"
    COBOL_UNISYS_QUEUE_NAME: str = "cobol_unisys_queue"
    COBOL_DNP_QUEUE_NAME: str = "cobol_dnp_queue"
    COBOL_UNISYS_QUEUE_NAME: str = "cobol_unisys_queue"
    GRAPH_QUEUE_NAME: str = "graph_queue"
    COBOL_SUMMARIZATION_QUEUE_NAME: str = "cobol_summarization_queue"
    STATEMENT_SUMMARIZATION_QUEUE_NAME: str = "statement_summarization_queue"
    ASSESSMENT_QUEUE_NAME: str = "assessment_queue"
    WFL_QUEUE_NAME: str = "wfl_queue"
    BMS_MODERNIZATION_QUEUE_NAME: str = "bms_modernization_queue"
    COBOL_UNISYS_RESPONSE_QUEUE_NAME: str = "cobol_unisys_response_queue"
    BMS_MODERNIZATION_RESPONSE_QUEUE_NAME: str = "bms_modernization_response_queue"
    COBOL_SUMMARIZATION_RESPONSE_QUEUE_NAME: str = "cobol_summarization_response_queue"
    

    # Exchange Names
    EMAIL_EXCHANGE_NAME: str = "email_exchange"
    NOTIFICATION_EXCHANGE_NAME: str = "notification_exchange"
    PROCESSING_EXCHANGE_NAME: str = "processing_exchange"
    PARSER_EXCHANGE_NAME: str = "parser_exchange"
    MODERNIZATION_EXCHANGE_NAME: str = "parser_exchange"
    SUMMARIZATION_EXCHANGE_NAME: str = "summarization_exchange"
    MIGRATION_EXCHANGE_NAME: str = "migration_exchange"

    # Routing Keys
    EMAIL_ROUTING_KEY: str = "email.*"
    NOTIFICATION_ROUTING_KEY: str = "notification.*"
    PROCESSING_ROUTING_KEY: str = "processing.*"
    BMS_SUMMARIZATION_ROUTING_KEY: str = "summarization.bms"
    COBOL_SCREEN_SUMMARIZATION_ROUTING_KEY: str = "summarization.screen.cobol"
    COBOL_JAVA_MIGRATION_ROUTING_KEY: str = "migration.java.cobol"
    BMS_JAVA_MIGRATION_ROUTING_KEY: str = "migration.java.bms"
    BAT_ROUTING_KEY: str = "parser.bat"
    COBOL_DISPATCHER_ROUTING_KEY: str = "parser.dispatcher.cobol"
    WFL_DISPATCHER_ROUTING_KEY: str = "parser.dispatcher.wfl"
    SCREEN_ACCESS_ROUTING_KEY: str = "parser.screen_access"
    COBOL_UNISYS_ROUTING_KEY: str = "parser.cobol.unisys"
    COBOL_DNP_ROUTING_KEY: str = "parser.cobol.dnp"
    GRAPH_ROUTING_KEY: str = "parser.graph"
    COPYBOOK_DNP_ROUTING_KEY: str = "parser.copybook.dnp"
    COPYBOOK_UNISYS_ROUTING_KEY: str = "parser.copybook.unisys"
    COBOL_SUMMARIZATION_ROUTING_KEY: str = "cobol.summarization"
    STATEMENT_SUMMARIZATION_ROUTING_KEY: str = "statement.summarization"
    ASSESSMENT_ROUTING_KEY: str = "parser.assessment"
    CLIST_ROUTING_KEY: str = "parser.clist"
    CLIST_DISPATCHER_ROUTING_KEY: str = "parser.dispatcher.clist"
    PANEL_ROUTING_KEY: str = "parser.panel"
    PANEL_DISPATCHER_ROUTING_KEY: str = "parser.dispatcher.panel"
    REPORT_ROUTING_KEY: str = "parser.report"
    REPORT_DISPATCHER_ROUTING_KEY: str = "parser.dispatcher.report"
    WFL_ROUTING_KEY: str = "parser.wfl"
    BMS_MODERNIZATION_ROUTING_KEY: str = "modernize.bms"
    COBOL_UNISYS_RESPONSE_ROUTING_KEY: str = "parser.cobol.unisys.response"
    BMS_MODERNIZATION_RESPONSE_ROUTING_KEY: str = "modernize.bms.response"
    COBOL_SUMMARIZATION_RESPONSE_ROUTING_KEY: str = "cobol.summarization.response"

    # Requeue settings
    DELAY_QUEUE_SUFFIX: str = ".delay"
    RETRY_COUNT_HEADER: str = "x-retry-count"
    LAST_ERROR_HEADER: str = "x-last-error"
    ORIGINAL_ROUTING_KEY_HEADER: str = "x-original-routing-key"
    TTL_HEADER: str = "x-message-ttl"
    DLX_HEADER: str = "x-dead-letter-exchange"
    DLX_ROUTING_KEY_HEADER: str = "x-dead-letter-routing-key"

    # MongoDB settings
    MONGODB_HOST: str = "localhost"
    MONGODB_PORT: str = "27017"
    MONGODB_USER: str | None = None
    MONGODB_PASSWORD: str | None = None
    MONGODB_DB_NAME: str = "cobol_analyzer"

    # Redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str | None = None

    # Other
    COBOL_VERBS_FILE: str = "cobol_verbs.txt"
    JCL_KEYWORDS_FILE: str = "jcl_keywords.txt"
    KOOPA_CACHE_DIR: str = "./tmp"
    
    # Airflow
    REVERSE_REPO_EXECUTION_TIMEOUT: int = 3600
    REVERSE_REPO_TIMEOUT: int = 3600

    @property
    def QUEUE_CONFIGS(self) -> Dict[str, QueueConfig]:
        return {
            "email_tasks": QueueConfig(
                name=self.EMAIL_QUEUE_NAME,
                exchange=self.EMAIL_EXCHANGE_NAME,
                routing_key=self.EMAIL_ROUTING_KEY,
            ),
            "notification_tasks": QueueConfig(
                name=self.NOTIFICATION_QUEUE_NAME,
                exchange=self.NOTIFICATION_EXCHANGE_NAME,
                routing_key=self.NOTIFICATION_ROUTING_KEY,
            ),
            "processing_tasks": QueueConfig(
                name=self.PROCESSING_QUEUE_NAME,
                exchange=self.PROCESSING_EXCHANGE_NAME,
                routing_key=self.PROCESSING_ROUTING_KEY,
            ),
            "cobol_dispatcher": QueueConfig(
                name=self.COBOL_DISPATCHER_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COBOL_DISPATCHER_ROUTING_KEY,
            ),
            "wfl_dispatcher": QueueConfig(
                name=self.WFL_DISPATCHER_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.WFL_DISPATCHER_ROUTING_KEY,
            ),
            "bms_summarization": QueueConfig(
                name=self.BMS_SUMMARIZATION_QUEUE_NAME,
                exchange=self.SUMMARIZATION_EXCHANGE_NAME,
                routing_key=self.BMS_SUMMARIZATION_ROUTING_KEY,
            ),
            "cobol_screen_summarization": QueueConfig(
                name=self.COBOL_SCREEN_SUMMARIZATION_QUEUE_NAME,
                exchange=self.SUMMARIZATION_EXCHANGE_NAME,
                routing_key=self.COBOL_SCREEN_SUMMARIZATION_ROUTING_KEY,
            ),
            "cobol_java_migration": QueueConfig(
                name=self.COBOL_JAVA_MIGRATION_QUEUE_NAME,
                exchange=self.MIGRATION_EXCHANGE_NAME,
                routing_key=self.COBOL_JAVA_MIGRATION_ROUTING_KEY,
            ),
            "bms_java_migration": QueueConfig(
                name=self.BMS_JAVA_MIGRATION_QUEUE_NAME,
                exchange=self.MIGRATION_EXCHANGE_NAME,
                routing_key=self.BMS_JAVA_MIGRATION_ROUTING_KEY,
            ),
            "bat_tasks": QueueConfig(
                name=self.BAT_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.BAT_ROUTING_KEY,
            ),
            "cobol_unisys_tasks": QueueConfig(
                name=self.COBOL_UNISYS_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COBOL_UNISYS_ROUTING_KEY,
            ),
            "cobol_dnp_tasks": QueueConfig(
                name=self.COBOL_DNP_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COBOL_DNP_ROUTING_KEY,
            ),
            "graph_tasks": QueueConfig(
                name=self.GRAPH_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.GRAPH_ROUTING_KEY,
            ),
            "copybook_dnp_tasks": QueueConfig(
                name=self.COPYBOOK_DNP_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COPYBOOK_DNP_ROUTING_KEY,
            ),
            "assessment_tasks": QueueConfig(
                name=self.ASSESSMENT_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.ASSESSMENT_ROUTING_KEY,
            ),
            "copybook_unisys_tasks": QueueConfig(
                name=self.COPYBOOK_UNISYS_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COPYBOOK_UNISYS_ROUTING_KEY,
            ),
            "cobol_summarization": QueueConfig(
                name=self.COBOL_SUMMARIZATION_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COBOL_SUMMARIZATION_ROUTING_KEY,
            ),
            "statement_summarization": QueueConfig(
                name=self.STATEMENT_SUMMARIZATION_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.STATEMENT_SUMMARIZATION_ROUTING_KEY,
            ),
            "wfl_tasks": QueueConfig(
                name=self.WFL_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.WFL_ROUTING_KEY,
            ),
            "bms_modernization": QueueConfig(
                name=self.BMS_MODERNIZATION_QUEUE_NAME,
                exchange=self.MODERNIZATION_EXCHANGE_NAME,
                routing_key=self.BMS_MODERNIZATION_ROUTING_KEY,
            ),
            "cobol_unisys_response_tasks": QueueConfig(
                name=self.COBOL_UNISYS_RESPONSE_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COBOL_UNISYS_RESPONSE_ROUTING_KEY,
            ),
            "bms_modernization_response": QueueConfig(
                name=self.BMS_MODERNIZATION_RESPONSE_QUEUE_NAME,
                exchange=self.MODERNIZATION_EXCHANGE_NAME,
                routing_key=self.BMS_MODERNIZATION_RESPONSE_ROUTING_KEY,
            ),
            "cobol_summarization_response_tasks": QueueConfig(
                name=self.COBOL_SUMMARIZATION_RESPONSE_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.COBOL_SUMMARIZATION_RESPONSE_ROUTING_KEY,
            ),
            "clist_tasks": QueueConfig(
                name = self.CLIST_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.CLIST_ROUTING_KEY
            ),
            "clist_dispatcher": QueueConfig(
                name = self.CLIST_DISPATCHER_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.CLIST_DISPATCHER_ROUTING_KEY,
            ),
            "panel_tasks": QueueConfig(
                name = self.PANEL_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.PANEL_ROUTING_KEY
            ),
            "panel_dispatcher": QueueConfig(
                name = self.PANEL_DISPATCHER_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.PANEL_DISPATCHER_ROUTING_KEY,
            ),
            "report_tasks": QueueConfig(
                name = self.REPORT_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.REPORT_ROUTING_KEY
            ),
            "report_dispatcher": QueueConfig(
                name = self.REPORT_DISPATCHER_QUEUE_NAME,
                exchange=self.PARSER_EXCHANGE_NAME,
                routing_key=self.REPORT_DISPATCHER_ROUTING_KEY,
            ),
        }

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
