"""
Core data types for agent communication.
"""

from pathlib import Path

from pydantic import BaseModel

from .enums import MimeType


class Document(BaseModel):
    """A document with metadata and content."""

    file_path: Path
    mime_type: MimeType
