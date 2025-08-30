from enum import Enum
from loguru import logger
from langchain.chat_models import init_chat_model
from typing import Literal
from config.settings import settings

class LLMProvider(Enum):
    AZURE_OPENAI = "azure_openai"

ModelType = Literal["default", "assistant"]

def get_llm(model_type: ModelType = "default"):
    try:
        # Select model configuration based on type
        if model_type == "assistant":
            model_name = settings.AZURE_OPENAI_MODEL
            model_kwargs = {
                "temperature": settings.ASSISTANT_AGENT_TEMPERATURE,
                "top_p": settings.ASSISTANT_AGENT_TOP_P,
                "frequency_penalty": settings.ASSISTANT_AGENT_FREQUENCY_PENALTY,
                "presence_penalty": settings.ASSISTANT_AGENT_PRESENCE_PENALTY,
            }
        else:
            model_kwargs = {}

        if settings.LLM_PROVIDER == LLMProvider.AZURE_OPENAI.value:
            model = init_chat_model(
                model_name,
                model_provider=settings.LLM_PROVIDER,
                api_key=settings.AZURE_OPENAI_API_KEY,
                api_version=settings.AZURE_OPENAI_API_VERSION,
                azure_endpoint=settings.AZURE_OPENAI_API_BASE,
                **model_kwargs
            )
        else:
            supported_providers = ", ".join(
                [provider.value for provider in LLMProvider]
            )
            raise ValueError(
                f"Unsupported LLM provider: '{settings.LLM_PROVIDER.value}', currently support {supported_providers}",
            )
        return model
    except Exception as e:
        logger.error(f"Error initializing LLM: {str(e)}")
        raise
