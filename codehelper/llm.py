"""Module containing LLM interface logic."""

from langchain.chat_models import ChatOpenAI
from typing import Any, Dict

from django.conf import settings


class LLM:
    # TODO
    def __init__(
        self,
        model_name: str = "gpt-3.5-turbo-16k",
        temperature: float = 0.2,
        max_tokens: int = 10000,
        model_kwargs: Dict[str, Any] = {
            'frequency_penalty': 0.2,
            'presence_penalty': 0,
        }
    ):
        self.model = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            model_kwargs=model_kwargs,
            openai_api_key=settings.OPENAI_API_KEY,
        )
