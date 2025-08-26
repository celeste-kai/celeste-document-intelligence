from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider

# Capability for this domain package
CAPABILITY: Capability = Capability.DOCUMENT_INTELLIGENCE

# Provider wiring for document intelligence clients
PROVIDER_MAPPING: dict[Provider, tuple[str, str]] = {
    Provider.GOOGLE: (".providers.google", "GeminiDocClient"),
}

__all__ = ["CAPABILITY", "PROVIDER_MAPPING"]
