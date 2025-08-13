"""
Core enumerations for Celeste AI Client.
"""

from enum import Enum


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
