# app/llm/factory.py

from app.config.settings import LLM_PROVIDER

from app.llm.ollama_provider import OllamaProvider
from app.llm.openai_provider import OpenAIProvider


def get_llm():

    if LLM_PROVIDER == "ollama":
        return OllamaProvider()

    elif LLM_PROVIDER == "openai":
        return OpenAIProvider()

    raise Exception(
        "Unsupported provider"
    )