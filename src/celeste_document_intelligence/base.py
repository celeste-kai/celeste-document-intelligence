from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Optional, List

from .core.types import AIResponse, AIUsage

from .core.types import Document


class BaseDocClient(ABC):
    def __init__(self, **kwargs: Any) -> None:
        """
        Initializes the client, loading credentials from the environment.
        Provider-specific arguments can be passed via kwargs.
        """
        pass

    @abstractmethod
    async def generate_content(
        self, prompt: str, documents: List[Document], **kwargs: Any
    ) -> AIResponse:
        """Generates a single response."""
        pass

    @abstractmethod
    def stream_generate_content(
        self, prompt: str, documents: List[Document], **kwargs: Any
    ) -> AsyncIterator[AIResponse]:
        """Streams the response chunk by chunk."""
        pass

    @abstractmethod
    def format_usage(self, usage_data: Any) -> Optional[AIUsage]:
        """Convert provider-specific usage data to standardized AIUsage format."""
        pass
