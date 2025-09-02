# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `celeste-document-intelligence`, a Python package that provides multi-provider document processing capabilities. It's part of the larger Celeste AI ecosystem and focuses specifically on document intelligence operations like PDF analysis, text extraction, and document understanding through AI models.

## Architecture

### Core Components
- **Document Client Factory**: `create_doc_client()` function creates provider-specific clients
- **Provider System**: Currently implements Google Gemini, with planned support for OpenAI, Mistral, Anthropic, HuggingFace, and Ollama
- **Document Types**: `Document` class with `file_path` and `mime_type` properties
- **MIME Type Support**: Comprehensive enum covering PDF, text, code files, HTML, CSV, XML, RTF

### Key Files
- `src/celeste_document_intelligence/__init__.py`: Main entry point and client factory
- `src/celeste_document_intelligence/core/types.py`: Document data model
- `src/celeste_document_intelligence/core/enums.py`: MimeType definitions
- `src/celeste_document_intelligence/mapping.py`: Provider-to-implementation mapping
- `src/celeste_document_intelligence/providers/google.py`: Google Gemini implementation
- `example.py`: Streamlit demo application

### Dependencies
- Depends on `celeste-core` package from GitHub (provides base classes, providers, settings)
- Uses `google-genai` for Google provider implementation
- Built with Pydantic for data validation

## Development Commands

### Package Management
```bash
uv sync                    # Install dependencies
uv add <package>          # Add new dependency
```

### Code Quality
```bash
ruff check                # Linting
ruff format               # Code formatting  
mypy src/                 # Type checking
```

### Pre-commit Hooks
```bash
pre-commit install        # Install hooks
pre-commit run --all-files # Run all hooks
```

### Running the Demo
```bash
streamlit run example.py  # Start Streamlit demo app
```

### Testing
No test suite is currently implemented - this would be a good area for contribution.

## Provider Implementation Pattern

When adding new providers:
1. Create provider class in `src/celeste_document_intelligence/providers/`
2. Inherit from `BaseDocClient` from `celeste-core` 
3. Implement required methods: `generate_content()` and `stream_generate_content()`
4. Add provider mapping in `mapping.py`
5. Ensure provider validation is handled via `celeste-core` settings

## Environment Configuration

The package uses `celeste-core` settings for API key management. Currently supports:
- `GOOGLE_API_KEY` for Google Gemini models

## Important Notes

- Always use `uv add` instead of `pip install` for dependencies
- The package follows the Celeste ecosystem's provider pattern with capability-based model selection
- Document processing is async-first with both streaming and non-streaming interfaces
- Models are managed centrally through `celeste-core` catalog system