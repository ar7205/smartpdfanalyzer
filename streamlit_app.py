# Advanced Streamlit UI — Smart AI PDF Analyzer
import streamlit as st 
import tempfile
import pdfplumber

from app.rag_pipeline import (
    process_pdf,
    ask_question
)

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Smart AI PDF Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>

/* Main App */
.stApp {
    background: linear-gradient(to bottom right, #0f172a, #020617);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Glass Cards */
.glass-card {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 22px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
    text-align: center;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.05);
    border-radius: 18px;
    padding: 10px;
    border: 1px solid rgba(255,255,255,0.05);
}

/* Chat Input */
[data-testid="stChatInput"] {
    border-radius: 20px;
}

/* Buttons */
.stButton button {
    border-radius: 12px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05);
    border-radius: 18px;
    padding: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Headings */
h1, h2, h3 {
    color: white;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================
with st.sidebar:

    st.markdown("# ⚡ Smart AI PDF Analyzer")

    st.caption("Enterprise-style RAG application")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "📄 Upload PDF",
        type="pdf"
    )
    if uploaded_file:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:
            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        if "vector_store" not in st.session_state:
            with st.spinner("Processing PDF..."):
                data = process_pdf(pdf_path)
                st.session_state.vector_store = data["vector_store"]
                st.session_state.total_chunks = data["total_chunks"]
                st.session_state.text_length = data["text_length"]
                with pdfplumber.open(pdf_path) as pdf:
                    st.session_state.num_pages = len(pdf.pages)
            st.success("PDF processed successfully! 🚀")

    st.markdown("---")

    st.subheader("🚀 Features")

    st.write("✅ Semantic Search")
    st.write("✅ HuggingFace Embeddings")
    st.write("✅ FAISS Vector Retrieval")
    st.write("✅ Ollama Local AI")
    st.write("✅ RAG Pipeline")

    st.markdown("---")

    st.info(
        "Upload PDFs and chat with them using AI-powered retrieval."
    )

# =====================================
# HERO SECTION
# =====================================
st.markdown("""
<div class="glass-card">
    <h1>📄 Smart AI PDF Analyzer</h1>
    <p style='font-size:18px;'>
        AI-powered semantic PDF search using embeddings, vector retrieval, and Gemini AI.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# DASHBOARD METRICS
# =====================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📄 Pages",
        st.session_state.get("num_pages", 0)
    )

with col2:
    st.metric(
        "✂️ Chunks",
        st.session_state.get(
            "total_chunks",
            0
        )
    )

with col3:
    st.metric(
        "🧠 Embeddings",
        384
    )

with col4:
    st.metric("⚡ Retrieval Speed", "0ms")

st.write("")

# =====================================
# MAIN LAYOUT
# =====================================
left_col, right_col = st.columns([1, 1.5])

# =====================================
# LEFT PANEL
# =====================================
with left_col:

    if "vector_store" in st.session_state:
        total_chunks = st.session_state.get("total_chunks", 0)
        text_length = st.session_state.get("text_length", 0)
        st.markdown(f"""
        <div class="glass-card">
            <h3>📑 Document Insights</h3>
            <p style='margin-bottom:8px;'><b>Total Chunks:</b> {total_chunks}</p>
            <p style='margin-bottom:8px;'><b>Character Count:</b> {text_length}</p>
            <p style='margin-bottom:8px;'><b>Vector Dimension:</b> 384 (MiniLM-L6-v2)</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="glass-card">
            <h3>📑 Document Insights</h3>
            <p>PDF analytics and processing details will appear here.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if "last_retrieved_chunks" in st.session_state and st.session_state.last_retrieved_chunks:
        chunks_html = ""
        for i, chunk in enumerate(st.session_state.last_retrieved_chunks):
            clean_chunk = chunk.replace("<", "&lt;").replace(">", "&gt;")
            chunks_html += f"""
            <div style='background: rgba(255, 255, 255, 0.03); padding: 12px; border-radius: 10px; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.05); font-size: 13.5px; line-height: 1.4; color: #e2e8f0;'>
                <span style='color: #818cf8; font-weight: 600;'>Chunk {i+1}:</span> {clean_chunk}
            </div>
            """
        st.markdown(f"""
        <div class="glass-card" style="max-height: 500px; overflow-y: auto;">
            <h3>🔍 Retrieval Inspector</h3>
            <p style='font-size:14px; color:#94a3b8; margin-bottom:12px;'>Top semantic chunks retrieved by FAISS for your last query:</p>
            {chunks_html}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="glass-card">
            <h3>🔍 Retrieval Inspector</h3>
            <p>
                Top semantic chunks retrieved by FAISS will appear here.
            </p>
        </div>
        """, unsafe_allow_html=True)

# =====================================
# RIGHT PANEL
# =====================================
with right_col:

    st.markdown("""
    <div class="glass-card">
        <h3>💬 Chat with your PDF</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Chat Input
    question = st.chat_input(
        "Ask anything about your PDF..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            with st.spinner("Analyzing PDF using AI..."):
                if "vector_store" in st.session_state:
                    answer, retrieved_chunks = ask_question(
                        question,
                        st.session_state.vector_store
                    )
                    fake_answer = answer
                    st.session_state.last_retrieved_chunks = retrieved_chunks
                else:
                    fake_answer = "Please upload a PDF first."
                
                st.write(fake_answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": fake_answer
        })

# =====================================
# FOOTER
# =====================================
st.write("")
st.markdown("---")

st.caption(
    "Built with Streamlit • HuggingFace • FAISS • Gemini"
)
