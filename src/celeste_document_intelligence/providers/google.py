from typing import Any, Dict, Optional, List
from google import genai
from google.genai import types
from typing import AsyncIterator

from ..base import BaseDocClient
from ..core.config import GOOGLE_API_KEY
from ..core.enums import GeminiModel
from ..core.types import AIUsage, Document, AIResponse
from ..core.enums import Provider


class GeminiDocClient(BaseDocClient):
    def __init__(
        self, model: str = GeminiModel.FLASH_LITE.value, **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)

        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        self.model_name = model

    @staticmethod
    def _get_generation_config(kwargs: Dict[str, Any]) -> types.GenerateContentConfig:
        """Get or create generation config with the default thinking budget."""
        return kwargs.pop(
            "config",
            types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=-1)
            ),
        )

    def format_usage(self, usage_data: Any) -> Optional[AIUsage]:
        """Convert Gemini usage data to AIUsage."""
        if not usage_data:
            return None
        return AIUsage(
            input_tokens=getattr(usage_data, "prompt_token_count", 0),
            output_tokens=getattr(usage_data, "candidates_token_count", 0),
            total_tokens=getattr(usage_data, "total_token_count", 0),
        )

    async def generate_content(
        self, prompt: str, documents: List[Document], **kwargs: Any
    ) -> AIResponse:
        """Generate text from a prompt and a list of documents."""
        response = await self.client.aio.models.generate_content(
            model=self.model_name,
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

        # Convert usage data if available
        usage = self.format_usage(getattr(response, "usage_metadata", None))

        # Return AIResponse object
        return AIResponse(
            text=response.text,
            usage=usage,
            provider=Provider.GOOGLE,
            metadata={"model": self.model_name},
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

        last_usage_metadata = None
        async for chunk in await self.client.aio.models.generate_content_stream(
            model=self.model_name, contents=contents, config=config
        ):
            if chunk.text:  # Only yield if there's actual content
                yield AIResponse(
                    text=chunk.text,
                    provider=Provider.GOOGLE,
                    metadata={"model": self.model_name, "is_stream_chunk": True},
                )
            if hasattr(chunk, "usage_metadata") and chunk.usage_metadata:
                last_usage_metadata = chunk.usage_metadata

        usage = self.format_usage(last_usage_metadata)
        if usage:
            yield AIResponse(
                text="",  # Empty content for the usage-only response
                usage=usage,
                provider=Provider.GOOGLE,
                metadata={"model": self.model_name, "is_final_usage": True},
            )
