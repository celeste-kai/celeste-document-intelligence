"""
Celeste Document Intelligence - Multi-provider document processing client for Python.
"""

from typing import Any

from celeste_core import Provider
from celeste_core.base.document_client import BaseDocClient
from celeste_core.config.settings import settings

from .core.enums import MimeType
from .core.types import Document

__version__ = "0.1.0"

SUPPORTED_PROVIDERS: set[Provider] = {Provider.GOOGLE}


def create_doc_client(provider: str, **kwargs: Any) -> BaseDocClient:
    provider_enum = Provider(provider) if isinstance(provider, str) else provider
    if provider_enum not in SUPPORTED_PROVIDERS:
        supported = [p.value for p in SUPPORTED_PROVIDERS]
        raise ValueError(
            f"Unsupported provider: {provider_enum.value}. Supported: {supported}"
        )

    # Validate environment for the chosen provider
    settings.validate_for_provider(provider_enum.value)

    mapping = {
        Provider.GOOGLE: (".providers.google", "GeminiDocClient"),
    }

    module_path, class_name = mapping[provider_enum]
    module = __import__(
        f"celeste_document_intelligence{module_path}",
        fromlist=[class_name],
    )
    client_class = getattr(module, class_name)
    return client_class(**kwargs)


__all__ = [
    "create_doc_client",
    "BaseDocClient",
    "Provider",
    "Document",
    "MimeType",
]
