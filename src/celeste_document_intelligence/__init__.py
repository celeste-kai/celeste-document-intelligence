"""
Celeste Document Intelligence - Multi-provider document processing client for Python.
"""

from typing import Any

from .base import BaseDocClient
from .core.types import AIResponse, AIUsage, Document
from .core.enums import DocumentIntelligenceProvider, MimeType, GeminiModel

__version__ = "0.1.0"

SUPPORTED_PROVIDERS = [
    "google",
]


def create_doc_client(provider: str, **kwargs: Any) -> BaseDocClient:
    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    if provider == "google":
        from .providers.google import GeminiDocClient

        return GeminiDocClient(**kwargs)
    # Other providers to be implemented

    raise ValueError(f"Provider {provider} not implemented")


__all__ = [
    "create_doc_client",
    "BaseDocClient",
    "DocumentIntelligenceProvider",
    "AIResponse",
    "AIUsage",
    "Document",
    "MimeType",
    "GeminiModel",
]
