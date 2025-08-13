import asyncio
from pathlib import Path
from typing import List, Tuple

import streamlit as st
from celeste_core import AIResponse, list_models
from celeste_core.enums.capability import Capability
from src.celeste_document_intelligence import create_doc_client
from src.celeste_document_intelligence.core.enums import MimeType
from src.celeste_document_intelligence.core.types import Document

st.set_page_config(
    page_title="Celeste Document Intelligence", page_icon="📄", layout="wide"
)

st.title("📄 Celeste Document Intelligence")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")

    # Provider selection from registry by DOCUMENT_INTELLIGENCE capability
    providers = sorted(
        {m.provider for m in list_models(capability=Capability.DOCUMENT_INTELLIGENCE)},
        key=lambda p: p.value,
    )
    selected_provider = providers[0].value if providers else "google"
    st.info(f"Provider: {selected_provider.title()}")

    # Model selection from registry
    models = list_models(
        provider=providers[0], capability=Capability.DOCUMENT_INTELLIGENCE
    )
    display = [m.display_name or m.id for m in models]
    id_by_display = {d: models[i].id for i, d in enumerate(display)}
    selected_display = st.selectbox("Model:", options=display, index=0)
    selected_model = id_by_display[selected_display]

    st.divider()

    # PDF file selection
    st.header("📄 Document Selection")

    # Get PDF files from data directory
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

    # File uploader as alternative
    uploaded_file = st.file_uploader("Or upload a PDF:", type=["pdf"])

    streaming = st.toggle("Enable Streaming", value=False)

st.markdown("*Powered by Google Gemini*")

# Main interface
prompt = st.text_area(
    "Enter your prompt:",
    value="Provide a summary of the document.",
    height=100,
    placeholder="Ask me anything about the document...",
)

if st.button("✨ Generate", type="primary", use_container_width=True):
    # Determine which PDF to use
    pdf_path = None
    if uploaded_file:
        # Save uploaded file temporarily
        temp_path = Path("temp_upload.pdf")
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        pdf_path = temp_path
    elif selected_pdf:
        pdf_path = selected_pdf

    if not pdf_path:
        st.error("Please select or upload a PDF file.")
    else:
        client = create_doc_client(selected_provider, model=selected_model)

        # Create the Document
        document = Document(file_path=pdf_path, mime_type=MimeType.PDF)

        # Show Document details in an expander
        with st.expander("🔍 Document Details", expanded=False):
            doc_dict = {
                "file_path": str(document.file_path),
                "mime_type": document.mime_type.value,
            }
            st.json(doc_dict)

        if streaming:
            placeholder = st.empty()
            response_chunks: List[AIResponse] = []

            async def stream_response() -> Tuple[str, List[AIResponse]]:
                response_text = ""
                async for chunk in client.stream_generate_content(
                    prompt, documents=[document]
                ):
                    response_chunks.append(chunk)

                    if chunk.text:
                        response_text += chunk.text
                        placeholder.markdown(f"**Response:**\n\n{response_text}▌")
                placeholder.markdown(f"**Response:**\n\n{response_text}")
                return response_text, response_chunks

            response_text, chunks = asyncio.run(stream_response())

            # Combine all chunks into a single response for display
            if chunks:
                # Find the last chunk with usage data
                final_usage = None
                for chunk in reversed(chunks):
                    if chunk.usage:
                        final_usage = chunk.usage
                        break

                # Create a combined response
                combined_response = AIResponse(
                    text=response_text,
                    provider=chunks[0].provider,
                    metadata=chunks[0].metadata,
                )

                with st.expander("📊 AIResponse Details", expanded=False):
                    response_dict = {
                        "text": combined_response.text,
                        "provider": combined_response.provider,
                        "usage": combined_response.usage.model_dump()
                        if combined_response.usage
                        else None,
                        "metadata": combined_response.metadata,
                    }
                    st.json(response_dict)
        else:
            with st.spinner("Generating..."):
                response = asyncio.run(
                    client.generate_content(prompt, documents=[document])
                )
                st.markdown(f"**Response:**\n\n{response.text}")

                # Show AIResponse details in an expander
                with st.expander("📊 AIResponse Details", expanded=False):
                    response_dict = {
                        "text": response.text,
                        "provider": response.provider,
                        "usage": response.usage.model_dump()
                        if response.usage
                        else None,
                        "metadata": response.metadata,
                    }
                    st.json(response_dict)

        # Clean up temporary file if it exists
        if uploaded_file and pdf_path.name == "temp_upload.pdf":
            pdf_path.unlink()

# Footer
st.markdown("---")
st.caption("Built with Streamlit • Powered by Google Gemini")
