from typing import Any, AsyncIterator, Dict, List

from celeste_core import AIResponse, Provider
from celeste_core.base.document_client import BaseDocClient
from celeste_core.config.settings import settings
from celeste_core.enums.capability import Capability
from google import genai
from google.genai import types

from ..core.types import Document


class GeminiDocClient(BaseDocClient):
    def __init__(
        self, model: str = "gemini-2.5-flash-lite-preview-06-17", **kwargs: Any
    ) -> None:
        super().__init__(
            model=model,
            capability=Capability.DOCUMENT_INTELLIGENCE,
            provider=Provider.GOOGLE,
            **kwargs,
        )
        self.client = genai.Client(api_key=settings.google.api_key)

    @staticmethod
    def _get_generation_config(kwargs: Dict[str, Any]) -> types.GenerateContentConfig:
        """Get or create generation config with the default thinking budget."""
        return kwargs.pop(
            "config",
            types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=-1)
            ),
        )

    async def generate_content(
        self, prompt: str, documents: List[Document], **kwargs: Any
    ) -> AIResponse:
        """Generate text from a prompt and a list of documents."""
        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=[
                prompt,
                *[
                    types.Part.from_bytes(
                        data=doc.file_path.read_bytes(),
                        mime_type=doc.mime_type.value,
                    )
                    for doc in documents
                ],
            ],
        )

        return AIResponse(
            content=response.text,
            provider=Provider.GOOGLE,
            metadata={"model": self.model},
        )

    async def stream_generate_content(
        self, prompt: str, documents: List[Document], **kwargs: Any
    ) -> AsyncIterator[AIResponse]:
        """Streams the response chunk by chunk."""
        config = self._get_generation_config(kwargs)
        contents = [
            prompt,
            *[
                types.Part.from_bytes(
                    data=doc.file_path.read_bytes(),
                    mime_type=doc.mime_type.value,
                )
                for doc in documents
            ],
        ]

        async for chunk in await self.client.aio.models.generate_content_stream(
            model=self.model, contents=contents, config=config
        ):
            if chunk.text:  # Only yield if there's actual content
                yield AIResponse(
                    content=chunk.text,
                    provider=Provider.GOOGLE,
                    metadata={"model": self.model, "is_stream_chunk": True},
                )
