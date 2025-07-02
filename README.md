<div align="center">

# 📄 Celeste Document Intelligence

### Advanced Document Processing and Analysis - Extract, Parse, and Understand Documents

[![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Providers](https://img.shields.io/badge/Providers-1_Implemented-orange?style=for-the-badge&logo=google&logoColor=white)](#-supported-providers)
[![Formats](https://img.shields.io/badge/Document_Formats-PDF_TXT_DOCX-purple?style=for-the-badge&logo=files&logoColor=white)](#-supported-formats)

[![Demo](https://img.shields.io/badge/🚀_Try_Demo-Jupyter-F37626?style=for-the-badge)](Notebooks/hello_world.ipynb)
[![Documentation](https://img.shields.io/badge/📚_Docs-Coming_Soon-blue?style=for-the-badge)](#)

</div>

---

## 🎯 Why Celeste?

<div align="center">
  <table>
    <tr>
      <td align="center">🔌<br><b>Unified API</b><br>One interface for all embedding providers</td>
      <td align="center">📊<br><b>Vector Output</b><br>Dense embeddings for your AI apps</td>
      <td align="center">⚡<br><b>Async First</b><br>Built for performance</td>
      <td align="center">📦<br><b>Batch Processing</b><br>Efficient bulk embeddings</td>
    </tr>
  </table>
</div>

## 🚀 Quick Start

```python
# Install
!uv add celeste-embeddings  # Coming soon to PyPI

# Use any embedding provider with the same interface
from celeste_embeddings import create_embedder
from celeste_embeddings.core.enums import GoogleEmbedding

# Create an embedder (currently Google is implemented)
embedder = create_embedder("google", model=GoogleEmbedding.GEMINIEMBEDDING)
# Generate embeddings for a single text
text = "The quick brown fox jumps over the lazy dog"
embedding = await embedder.embed(text)
```

## 📦 Installation

<details open>
<summary><b>Using UV (Recommended)</b></summary>

```bash
git clone https://github.com/yourusername/celeste-embeddings
cd celeste-embeddings
uv sync
```
</details>

<details>
<summary><b>Using pip</b></summary>

```bash
git clone https://github.com/yourusername/celeste-embeddings
cd celeste-embeddings
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

## 📊 Supported Embedding Models

<details>
<summary><b>View All Models</b></summary>

### 🌈 Google (Implemented)
- `text-embedding-004` - Latest Google embedding model (768 dimensions)
- `gemini-embedding-exp-03-07` - Experimental Gemini embeddings
- `embedding-001` - Legacy embedding model

### 🤖 OpenAI (Planned)
- `text-embedding-3-small` - Cost-effective embeddings
- `text-embedding-3-large` - High-quality embeddings
- `text-embedding-ada-002` - Legacy model

### 🌊 Mistral AI (Planned)
- `mistral-embed` - Mistral's embedding model

### 🎭 Anthropic (Planned)
- Anthropic embedding models (when available)

### 🤗 Hugging Face (Planned)
- `sentence-transformers/all-MiniLM-L6-v2` - Lightweight
- `sentence-transformers/all-mpnet-base-v2` - High quality
- `BAAI/bge-large-en-v1.5` - State-of-the-art
- [View more on HuggingFace](https://huggingface.co/models?pipeline_tag=sentence-similarity)

### 🦙 Ollama (Planned)
- `nomic-embed-text` - Nomic's embedding model
- `mxbai-embed-large` - High-performance embeddings
- [View all models](https://ollama.com/library?q=embed)

</details>

## 🎮 Interactive Demo

Try our Jupyter notebook example:

## 🗺️ Roadmap

### Celeste-Embeddings Next Steps
- [x] 📝 **Core Types** - Implement Embedding and AIUsage types
- [x] 🌈 **Google Provider** - Complete implementation with 3 models
- [ ] 🤖 **OpenAI Provider** - Add support for text-embedding-3 models
- [ ] 🌊 **Mistral Provider** - Add support for mistral-embed
- [ ] 🎭 **Anthropic Provider** - Add support when embeddings are available
- [ ] 🤗 **HuggingFace Provider** - Support for sentence-transformers
- [ ] 🦙 **Ollama Provider** - Local embedding models support
- [ ] 🧪 **Unit Tests** - Comprehensive test coverage
- [ ] 📚 **Documentation** - API documentation with examples
- [ ] 📦 **PyPI Package** - Publish to PyPI as `celeste-embeddings`

### Celeste Ecosystem

| Package | Description | Status |
|---------|-------------|--------|
| 🌟 **celeste-embeddings** | Text embeddings across providers | 🔄 This Package |
| 💬 **celeste-client** | Text generation and chat | ✅ Available |
| 💬 **celeste-conversations** | Multi-turn conversations with memory | 🔄 In Progress |
| 🌐 **celeste-web-agent** | Web browsing and automation | 📋 Planned |
| 🎨 **celeste-image-generation** | Image generation across providers | 📋 Planned |
| 🖼️ **celeste-image-intelligence** | Image analysis and understanding | 📋 Planned |
| 📄 **celeste-document-intelligence** | PDF and document processing | 📋 Planned |
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
  
  <a href="#-celeste-embeddings">⬆ Back to Top</a>
</div>