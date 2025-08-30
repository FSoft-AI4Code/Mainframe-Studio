from urllib.parse import quote_plus
from pydantic_settings import BaseSettings
from app.config import constants

class Settings(BaseSettings):
    # Basic App Settings
    APP_NAME: str
    DEBUG_MODE: bool
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # MongoDB Settings
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str
    MONGO_AUTH_SOURCE: str = "admin"
    MONGO_AUTH_MECHANISM: str = "SCRAM-SHA-256"

    @property
    def MONGO_URI(self) -> str:
        """Construct MongoDB URI from components."""
        username = quote_plus(self.MONGO_USER)
        password = quote_plus(self.MONGO_PASSWORD)

        return (
            f"mongodb://{username}:{password}"
            f"@{self.MONGO_HOST}:{self.MONGO_PORT}"
            f"/{self.MONGO_DATABASE}"
            f"?authSource={self.MONGO_AUTH_SOURCE}"
            f"&authMechanism={self.MONGO_AUTH_MECHANISM}"
        )
    
    # Redis Settings
    REDIS_URL: str

    # Azure OpenAI Settings
    AZURE_OPENAI_API_BASE: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_MODEL: str
    AZURE_OPENAI_MODEL_TYPE: str = "chat"
    AZURE_OPENAI_API_VERSION: str
    MODEL_NAME: str
    LLM_PROVIDER: constants.LLMProvider

    # Azure Storage Settings
    AZURE_STORAGE_CONNECTION_STRING: str
    AZURE_STORAGE_CONTAINER_NAME: str
    AZURE_WEB_DEPLOYMENT_URL: str = "https://cobolmigration.z12.web.core.windows.net"

    # Git Settings
    GIT_ASKPASS: str = "false"
    GIT_TERMINAL_PROMPT: str = "0"

    # Nebula Settings
    NEBULA_HOST: str
    NEBULA_PORT: str
    NEBULA_USERNAME: str
    NEBULA_PASSWORD: str
    NEBULA_MAX_CONNECTION_POOL_SIZE: int

    # Assistant Agent Settings
    ASSISTANT_AGENT_MODEL: str
    ASSISTANT_AGENT_TEMPERATURE: float = 0.0
    ASSISTANT_AGENT_MAX_TOKENS: int = 4000
    ASSISTANT_AGENT_TOP_P: float = 1.0
    ASSISTANT_AGENT_FREQUENCY_PENALTY: float = 0.0
    ASSISTANT_AGENT_PRESENCE_PENALTY: float = 0.0

    # RabbitMQ Settings
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_VHOST: str = "/"
    RABBITMQ_EXCHANGE: str = "parser_exchange"
    
    # Airflow Settings
    AIRFLOW_BASE_URL: str = "http://localhost:8080"
    AIRFLOW_USERNAME: str
    AIRFLOW_PASSWORD: str
    
    @property
    def RABBITMQ_URL(self) -> str:
        """Construct RabbitMQ URL from components."""
        credentials = f"{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}"
        return f"amqp://{credentials}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/{quote_plus(self.RABBITMQ_VHOST)}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()

def get_settings():
    return settings
