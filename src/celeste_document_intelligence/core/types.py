"""
Core data types for agent communication.
"""

from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict

from .enums import Provider, MimeType


class AIUsage(BaseModel):
    """Token usage metrics for AI responses."""

    model_config = ConfigDict(frozen=True)

    input_tokens: int
    output_tokens: int
    total_tokens: int


class AIResponse(BaseModel):
    """Response from AI providers."""

    text: str
    usage: Optional[AIUsage] = None
    provider: Optional[Provider] = None
    metadata: Dict[str, Any] = {}


class Document(BaseModel):
    """A document with metadata and content."""

    file_path: Path
    mime_type: MimeType
