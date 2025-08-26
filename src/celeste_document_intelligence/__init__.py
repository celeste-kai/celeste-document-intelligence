"""
Celeste Document Intelligence - Multi-provider document processing client for Python.
"""

from typing import Any

from celeste_core import Provider
from celeste_core.base.document_client import BaseDocClient
from celeste_core.config.settings import settings

from .core.enums import MimeType
from .core.types import Document
from .mapping import PROVIDER_MAPPING

__version__ = "0.1.0"


def create_doc_client(provider: str, **kwargs: Any) -> BaseDocClient:
    provider_enum = Provider(provider) if isinstance(provider, str) else provider
    if provider_enum not in PROVIDER_MAPPING:
        raise ValueError(f"Unsupported provider: {provider_enum}")

    # Validate environment for the chosen provider
    settings.validate_for_provider(provider_enum.value)

    if provider_enum not in PROVIDER_MAPPING:
        raise ValueError(f"No client mapping for provider: {provider_enum}")

    module_path, class_name = PROVIDER_MAPPING[provider_enum]
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
