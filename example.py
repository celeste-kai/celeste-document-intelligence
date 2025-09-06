import asyncio
from pathlib import Path
from typing import Any

import streamlit as st
from celeste_core import AIResponse, list_models
from celeste_core.enums.capability import Capability

from src.celeste_document_intelligence import create_doc_client
from src.celeste_document_intelligence.core.enums import MimeType
from src.celeste_document_intelligence.core.types import Document


def setup_sidebar() -> tuple[str, str, Path | None, Any, bool]:
    """Setup sidebar config and return provider, model, pdf file, uploaded file, streaming."""
    providers = sorted(
        {m.provider for m in list_models(capability=Capability.DOCUMENT_INTELLIGENCE)},
        key=lambda p: p.value,
    )

    with st.sidebar:
        st.header("⚙️ Configuration")
        provider = st.selectbox("Provider:", [p.value for p in providers], format_func=str.title)
        models = list_models(provider=providers[0], capability=Capability.DOCUMENT_INTELLIGENCE)
        model_names = [m.display_name or m.id for m in models]
        selected_idx = st.selectbox("Model:", range(len(models)), format_func=lambda i: model_names[i])
        model = models[selected_idx].id

        st.divider()

        st.header("📄 Document Selection")
        selected_pdf, uploaded_file = setup_file_selection()
        streaming = st.toggle("Enable Streaming", value=False)

    return provider, model, selected_pdf, uploaded_file, streaming


def setup_file_selection() -> tuple[Path | None, Any]:
    """Setup file selection interface and return selected PDF and uploaded file."""
    data_dir = Path("data")
    pdf_files = []
    if data_dir.exists():
        pdf_files = list(data_dir.glob("*.pdf"))

    if pdf_files:
        selected_pdf = st.selectbox(
            "Select PDF:",
            options=pdf_files,
            format_func=lambda x: x.name,
            index=0,
        )
    else:
        st.warning("No PDF files found in data directory")
        selected_pdf = None

    uploaded_file = st.file_uploader("Or upload a PDF:", type=["pdf"])
    return selected_pdf, uploaded_file


def get_pdf_path(uploaded_file: Any, selected_pdf: Path | None) -> Path | None:
    """Determine and return the PDF path to use."""
    if uploaded_file:
        temp_path = Path("temp_upload.pdf")
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return temp_path
    elif selected_pdf:
        return selected_pdf
    return None


def show_document_details(document: Document) -> None:
    """Show document details in an expander."""
    with st.expander("🔍 Document Details", expanded=False):
        doc_dict = {
            "file_path": str(document.file_path),
            "mime_type": document.mime_type.value,
        }
        st.json(doc_dict)


def show_response_details(provider: str, model: str, pdf_path: Path, response: AIResponse | None = None) -> None:
    """Show response details in an expander."""
    with st.expander("📊 Details", expanded=False):
        st.write(f"**Provider:** {provider}")
        st.write(f"**Model:** {model}")
        st.write(f"**Document:** {pdf_path.name}")
        if response and response.usage:
            st.json(response.usage.model_dump())


async def handle_streaming_response(
    client: Any, prompt: str, document: Document, provider: str, model: str, pdf_path: Path
) -> None:
    """Handle streaming response generation."""
    placeholder = st.empty()
    response_chunks: list[AIResponse] = []
    response_text = ""

    async for chunk in client.stream_generate_content(prompt, documents=[document]):
        response_chunks.append(chunk)
        if chunk.text:
            response_text += chunk.text
            placeholder.markdown(f"**Response:**\n\n{response_text}▌")

    placeholder.markdown(f"**Response:**\n\n{response_text}")

    if response_chunks:
        combined_response = AIResponse(
            text=response_text,
            provider=response_chunks[0].provider,
            metadata=response_chunks[0].metadata,
        )
        show_response_details(provider, model, pdf_path, combined_response)


async def handle_non_streaming_response(
    client: Any, prompt: str, document: Document, provider: str, model: str, pdf_path: Path
) -> None:
    """Handle non-streaming response generation."""
    with st.spinner("Generating..."):
        response = await client.generate_content(prompt, documents=[document])
        st.markdown(f"**Response:**\n\n{response.text}")
        show_response_details(provider, model, pdf_path, response)


async def main() -> None:
    st.set_page_config(page_title="Celeste Document Intelligence", page_icon="📄", layout="wide")
    st.title("📄 Celeste Document Intelligence")

    provider, model, selected_pdf, uploaded_file, streaming = setup_sidebar()
    st.markdown(f"*Powered by {provider.title()}*")

    prompt = st.text_area(
        "Enter your prompt:",
        value="Provide a summary of the document.",
        height=100,
        placeholder="Ask me anything about the document...",
    )

    if st.button("✨ Generate", type="primary", use_container_width=True):
        pdf_path = get_pdf_path(uploaded_file, selected_pdf)

        if not pdf_path:
            st.error("Please select or upload a PDF file.")
        else:
            client = create_doc_client(provider, model=model)
            document = Document(file_path=pdf_path, mime_type=MimeType.PDF)
            show_document_details(document)

            if streaming:
                await handle_streaming_response(client, prompt, document, provider, model, pdf_path)
            else:
                await handle_non_streaming_response(client, prompt, document, provider, model, pdf_path)

            # Clean up temporary file if it exists
            if uploaded_file and pdf_path.name == "temp_upload.pdf":
                pdf_path.unlink()

    st.markdown("---")
    st.caption("Built with Streamlit • Powered by Celeste")


if __name__ == "__main__":
    asyncio.run(main())
