import asyncio
from pathlib import Path
from typing import List

import streamlit as st
from celeste_core import AIResponse, list_models
from celeste_core.enums.capability import Capability
from src.celeste_document_intelligence import create_doc_client
from src.celeste_document_intelligence.core.enums import MimeType
from src.celeste_document_intelligence.core.types import Document


async def main() -> None:
    st.set_page_config(
        page_title="Celeste Document Intelligence", page_icon="📄", layout="wide"
    )

    st.title("📄 Celeste Document Intelligence")

    # Get providers that support document intelligence
    providers = sorted(
        {m.provider for m in list_models(capability=Capability.DOCUMENT_INTELLIGENCE)},
        key=lambda p: p.value,
    )

    with st.sidebar:
        st.header("⚙️ Configuration")
        provider = st.selectbox(
            "Provider:", [p.value for p in providers], format_func=str.title
        )
        models = list_models(
            provider=providers[0], capability=Capability.DOCUMENT_INTELLIGENCE
        )
        model_names = [m.display_name or m.id for m in models]
        selected_idx = st.selectbox(
            "Model:", range(len(models)), format_func=lambda i: model_names[i]
        )
        model = models[selected_idx].id

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

    st.markdown(f"*Powered by {provider.title()}*")

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
            client = create_doc_client(provider, model=model)

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

                response_text = ""
                async for chunk in client.stream_generate_content(
                    prompt, documents=[document]
                ):
                    response_chunks.append(chunk)

                    if chunk.text:
                        response_text += chunk.text
                        placeholder.markdown(f"**Response:**\n\n{response_text}▌")
                placeholder.markdown(f"**Response:**\n\n{response_text}")

                chunks = response_chunks

                # Combine all chunks into a single response for display
                if chunks:
                    # Create a combined response
                    combined_response = AIResponse(
                        text=response_text,
                        provider=chunks[0].provider,
                        metadata=chunks[0].metadata,
                    )

                    with st.expander("📊 Details", expanded=False):
                        st.write(f"**Provider:** {provider}")
                        st.write(f"**Model:** {model}")
                        st.write(f"**Document:** {pdf_path.name}")
                        if combined_response.usage:
                            st.json(combined_response.usage.model_dump())
            else:
                with st.spinner("Generating..."):
                    response = await client.generate_content(
                        prompt, documents=[document]
                    )
                    st.markdown(f"**Response:**\n\n{response.text}")

                    # Show response details in an expander
                    with st.expander("📊 Details", expanded=False):
                        st.write(f"**Provider:** {provider}")
                        st.write(f"**Model:** {model}")
                        st.write(f"**Document:** {pdf_path.name}")
                        if response.usage:
                            st.json(response.usage.model_dump())

            # Clean up temporary file if it exists
            if uploaded_file and pdf_path.name == "temp_upload.pdf":
                pdf_path.unlink()

    st.markdown("---")
    st.caption("Built with Streamlit • Powered by Celeste")


if __name__ == "__main__":
    asyncio.run(main())
