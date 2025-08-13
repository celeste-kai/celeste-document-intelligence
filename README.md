<div align="center">

# 📄 Celeste Document Intelligence

### Advanced Document Processing and Analysis - Extract, Parse, and Understand Documents

[![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Providers](https://img.shields.io/badge/Providers-1_Implemented-orange?style=for-the-badge&logo=google&logoColor=white)](#-supported-providers)
[![Formats](https://img.shields.io/badge/Document_Formats-PDF_TXT_DOCX-purple?style=for-the-badge&logo=files&logoColor=white)](#-supported-formats)

[![Demo](https://img.shields.io/badge/🚀_Try_Demo-Jupyter-F37626?style=for-the-badge)](Notebooks/demo.ipynb)
[![Documentation](https://img.shields.io/badge/📚_Docs-Coming_Soon-blue?style=for-the-badge)](#)

</div>

---

## 🎯 Why Celeste Document Intelligence?

<div align="center">
  <table>
    <tr>
      <td align="center">🔌<br><b>Unified API</b><br>One interface for all document AI providers</td>
      <td align="center">📄<br><b>Multi-Format</b><br>PDF, TXT, HTML, CSV, XML & more</td>
      <td align="center">⚡<br><b>Async First</b><br>Built for performance</td>
      <td align="center">🌊<br><b>Streaming</b><br>Real-time response streaming</td>
    </tr>
  </table>
</div>

## 🚀 Quick Start

```python
# Install
!uv add celeste-document-intelligence  # Coming soon to PyPI

# Process documents with AI
from celeste_document_intelligence import create_doc_client, Document, MimeType
from celeste_document_intelligence.core.enums import GeminiModel

# Create a client (currently Google Gemini is implemented)
client = create_doc_client("google", model=GeminiModel.FLASH)

# Create a document reference
doc = Document(
    file_path=Path("document.pdf"),
    mime_type=MimeType.PDF
)

# Ask questions about the document
response = await client.generate_content(
    prompt="Summarize this document",
    documents=[doc]
)

print(response.text)  # AI-generated summary
# Usage accounting is temporarily removed and will be reintroduced later
```

## 📦 Installation

<details open>
<summary><b>Using UV (Recommended)</b></summary>

```bash
git clone https://github.com/yourusername/celeste-document-intelligence
cd celeste-document-intelligence
uv sync
```
</details>

<details>
<summary><b>Using pip</b></summary>

```bash
git clone https://github.com/yourusername/celeste-document-intelligence
cd celeste-document-intelligence
pip install -e .
```
</details>

## 🔧 Configuration

### 1️⃣ Create your environment file
```bash
cp .env.example .env
```

### 2️⃣ Add your API keys

<details>
<summary><b>🔑 API Key Setup</b></summary>

| Provider | Environment Variable | Get API Key |
|----------|---------------------|-------------|
| 🌈 **Gemini** | `GOOGLE_API_KEY` | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| 🤖 **OpenAI** | `OPENAI_API_KEY` | [OpenAI Platform](https://platform.openai.com/api-keys) |
| 🌊 **Mistral** | `MISTRAL_API_KEY` | [Mistral Console](https://console.mistral.ai/) |
| 🎭 **Anthropic** | `ANTHROPIC_API_KEY` | [Anthropic Console](https://console.anthropic.com/) |
| 🤗 **Hugging Face** | `HUGGINGFACE_TOKEN` | [HF Settings](https://huggingface.co/settings/tokens) |
| 🦙 **Ollama** | *No key needed!* | [Install Ollama](https://ollama.com/download) |

</details>

## 🎨 Supported Providers

<div align="center">

| Provider | Status | Models | Batch Processing | Free Tier |
|----------|--------|--------|-----------------|------------|
| 🌈 **Google** | ✅ Implemented | 3 | ✅ | ✅ |
| 🤖 **OpenAI** | 🛠️ Planned | - | - | ❌ |
| 🌊 **Mistral AI** | 🛠️ Planned | - | - | ✅ |
| 🎭 **Anthropic** | 🛠️ Planned | - | - | ❌ |
| 🤗 **Hugging Face** | 🛠️ Planned | - | - | ✅ |
| 🦙 **Ollama** | 🛠️ Planned | - | - | ✅ |

</div>

## 📊 Supported Document Formats

<details>
<summary><b>View All Formats</b></summary>

### 📄 Documents
- **PDF** - Portable Document Format
- **TXT** - Plain text files
- **HTML** - Web pages
- **XML** - Structured data
- **RTF** - Rich Text Format
- **CSV** - Comma-separated values

### 💻 Code
- **Python** (.py)
- **JavaScript** (.js)
- **CSS** (.css)
- **Markdown** (.md)

### 🌈 AI Models (Currently Implemented)
- **Gemini 2.5 Flash Lite** - Fast, lightweight model
- **Gemini 2.5 Flash** - Balanced performance
- **Gemini 2.5 Pro** - Highest capability

</details>

## 🎮 Interactive Demo

Try our Jupyter notebook example: [Notebooks/demo.ipynb](Notebooks/demo.ipynb)

Or run the Streamlit app:
```bash
streamlit run example.py
```

## 🗺️ Roadmap

### Celeste-Document-Intelligence Next Steps
- [x] 📝 **Core Types** - Document and AIResponse
- [ ] 📊 **Usage Accounting** - Deferred; will be reintroduced later across modalities
- [x] 🌈 **Google Provider** - Gemini 2.5 models implementation
- [ ] 🤖 **OpenAI Provider** - GPT-4 Vision support
- [ ] 🌊 **Mistral Provider** - Document understanding models
- [ ] 🎭 **Anthropic Provider** - Claude 3 vision capabilities
- [ ] 📑 **More Formats** - DOCX, PPTX, XLSX support
- [ ] 🔍 **OCR Support** - Extract text from images in documents
- [ ] 🧪 **Unit Tests** - Comprehensive test coverage
- [ ] 📚 **Documentation** - API documentation with examples
- [ ] 📦 **PyPI Package** - Publish to PyPI as `celeste-document-intelligence`

### Celeste Ecosystem

| Package | Description | Status |
|---------|-------------|--------|
| 📄 **celeste-document-intelligence** | PDF and document processing | 🔄 This Package |
| 💬 **celeste-client** | Text generation and chat | ✅ Available |
| 💬 **celeste-conversations** | Multi-turn conversations with memory | 🔄 In Progress |
| 🌐 **celeste-web-agent** | Web browsing and automation | 📋 Planned |
| 🎨 **celeste-image-generation** | Image generation across providers | 📋 Planned |
| 🖼️ **celeste-image-intelligence** | Image analysis and understanding | 📋 Planned |
| 🌟 **celeste-embeddings** | Text embeddings across providers | 📋 Planned |
| 📈 **celeste-table-intelligence** | Excel, CSV, and Parquet analysis | 📋 Planned |
| 🎥 **celeste-video-intelligence** | Video analysis and understanding | 📋 Planned |
| 🚀 **And many more...** | Expanding ecosystem of AI tools | 🔮 Future |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ by the Celeste Team
  
  <a href="#-celeste-document-intelligence">⬆ Back to Top</a>
</div>