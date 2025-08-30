from langchain.chat_models import init_chat_model
from typing import Literal

from app.config import constants
from app.config.settings import get_settings

ModelType = Literal["default", "assistant"]

def get_llm(model_type: ModelType = "default"):
    settings = get_settings()
    
    # Select model configuration based on type
    if model_type == "assistant":
        model_name = settings.ASSISTANT_AGENT_MODEL
        model_kwargs = {
            "temperature": settings.ASSISTANT_AGENT_TEMPERATURE,
            "max_tokens": settings.ASSISTANT_AGENT_MAX_TOKENS,
            "top_p": settings.ASSISTANT_AGENT_TOP_P,
            "frequency_penalty": settings.ASSISTANT_AGENT_FREQUENCY_PENALTY,
            "presence_penalty": settings.ASSISTANT_AGENT_PRESENCE_PENALTY,
        }
    else:
        model_name = settings.MODEL_NAME
        model_kwargs = {}

    match settings.LLM_PROVIDER:
        case constants.LLMProvider.AZURE_OPENAI:
            model = init_chat_model(
                model_name,
                model_provider=settings.LLM_PROVIDER,
                api_key=settings.AZURE_OPENAI_API_KEY,
                api_version=settings.AZURE_OPENAI_API_VERSION,
                azure_endpoint=settings.AZURE_OPENAI_API_BASE,
                **model_kwargs
            )
        case _:
            supported_providers = ", ".join(
                [provider.value for provider in constants.LLMProvider]
            )
            raise ValueError(
                f"Unsupported LLM provider: '{settings.LLM_PROVIDER.value}', currently support {supported_providers}",
            )
    return model
