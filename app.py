import streamlit as st
from rag import load_pdf, create_index
from agent import agent

st.set_page_config(page_title="Offline PDF Chat", layout="wide")

st.title("📄 Chat with PDFs (Offline AI)")

st.info(
    "Ask clearly:\n"
    "- List my skills\n"
    "- What projects have I done?\n"
    "- Explain my experience\n"
)

# Session state
if "ready" not in st.session_state:
    st.session_state.ready = False

# Sidebar
with st.sidebar:
    st.header("Upload PDFs")

    pdf_files = st.file_uploader(
        "Upload your documents",
        accept_multiple_files=True
    )

    if st.button("Process"):
        if not pdf_files:
            st.warning("Please upload at least one PDF.")
        else:
            with st.spinner("Processing documents..."):
                try:
                    full_text = ""

                    for pdf in pdf_files:
                        full_text += load_pdf(pdf)

                    create_index(full_text)
                    st.session_state.ready = True

                    st.success("Documents processed successfully!")

                except Exception as e:
                    st.error(f"Error: {e}")

# Main query input
query = st.text_input("Ask a question:")

if query:
    if not st.session_state.ready:
        st.warning("Please upload and process documents first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = agent(query)

                st.write("### 🤖 Answer")
                st.write(response)

            except Exception as e:
                st.error(f"Error: {e}")