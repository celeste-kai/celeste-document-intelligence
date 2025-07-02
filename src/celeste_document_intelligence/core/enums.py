"""
Core enumerations for Celeste AI Client.
"""

from enum import Enum


class Provider(Enum):
    """AI provider enumeration for multi-provider agent support."""

    GOOGLE = "google"


class LogLevel(Enum):
    """Logging level enumeration for agent operations."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class GeminiModel(Enum):
    """Gemini 2.5 model enumeration for provider-specific model selection."""

    FLASH_LITE = "gemini-2.5-flash-lite-preview-06-17"
    FLASH = "gemini-2.5-flash"
    PRO = "gemini-2.5-pro"


class MimeType(Enum):
    """MIME type enumeration for document and content type identification."""

    PDF = "application/pdf"
    JAVASCRIPT = "application/x-javascript"
    JAVASCRIPT_TXT = "text/javascript"
    PYTHON = "application/x-python"
    PYTHON_TXT = "text/x-python"
    TEXT = "text/plain"
    HTML = "text/html"
    CSS = "text/css"
    MARKDOWN = "text/md"
    CSV = "text/csv"
    XML = "text/xml"
    RTF = "text/rtf"
