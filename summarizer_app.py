import streamlit as st
import io
import zipfile
import re
import time

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="YouTube Video → Article Generator",
    page_icon="🎥",
    layout="wide"
)

# -------------------------------
# Centered Layout CSS
# -------------------------------
st.markdown("""
<style>
.block-container {
    max-width: 750px;
    margin: auto;
}
body {
    background-color: #0d1117;
    color: #e6edf3;
}
.stTextInput input {
    background-color: #161b22;
    color: white;
}
.stButton button {
    width: auto !important;
    padding: 8px 18px;
    border-radius: 8px;
    background-color: #238636;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("🎥 YouTube Video → Article Generator")
st.markdown("Convert any YouTube video into a **professional article + webpage**")

# -------------------------------
# Sidebar Controls (NEW 🔥)
# -------------------------------
st.sidebar.header("⚙️ Controls")

model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["llama-3.1-8b-instant", "llama3-70b-8192"]
)

tone_choice = st.sidebar.selectbox(
    "Tone",
    ["Professional", "Casual", "Technical", "Beginner-Friendly"]
)

length_choice = st.sidebar.selectbox(
    "Length",
    ["Short", "Medium", "Detailed"]
)

fast_mode = st.sidebar.checkbox("⚡ Fast Mode")

generate_website = st.sidebar.checkbox("🌐 Generate Website (slower)")

# -------------------------------
# Input
# -------------------------------
youtube_url = st.text_input("Paste YouTube URL")

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    from summarizer_model import safe_summarize, extract_code_sections
    return safe_summarize, extract_code_sections

# -------------------------------
# Generate Article
# -------------------------------
@st.cache_data(show_spinner=False)
def generate_article(url, model, tone, length, fast):
    safe_summarize, _ = load_model()

    # Pass parameters if your model supports it
    try:
        return safe_summarize(
            url,
            model=model,
            tone=tone,
            length=length,
            fast_mode=fast
        )
    except:
        return safe_summarize(url)

# -------------------------------
# Clean Article
# -------------------------------
def clean_article(text):
    text = re.sub(r'--html--.*', '', text, flags=re.DOTALL)
    text = re.sub(r'<.*?>', '', text)
    return text.strip()

# -------------------------------
# Streaming Effect
# -------------------------------
def stream_text(text):
    placeholder = st.empty()
    displayed = ""
    for char in text:
        displayed += char
        placeholder.markdown(displayed)
        time.sleep(0.002)

# -------------------------------
# PDF
# -------------------------------
def create_pdf(text):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    clean_text = clean_article(text)

    content = []
    for line in clean_text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles["Normal"]))
            content.append(Spacer(1, 10))

    doc.build(content)
    buffer.seek(0)
    return buffer

# -------------------------------
# Session State
# -------------------------------
if "result" not in st.session_state:
    st.session_state.result = None

if "parsed" not in st.session_state:
    st.session_state.parsed = (None, None, None)

# -------------------------------
# Generate Button
# -------------------------------
if st.button("Generate Article 🚀"):

    if not youtube_url:
        st.warning("Please enter a YouTube URL")
    else:
        with st.spinner("Generating... ⏳"):

            result = generate_article(
                youtube_url,
                model_choice,
                tone_choice,
                length_choice,
                fast_mode
            )

            if not result or "ERROR" in str(result):
                st.error("❌ Failed to generate article")
            else:
                st.session_state.result = result

                if generate_website:
                    _, extract_code_sections = load_model()
                    st.session_state.parsed = extract_code_sections(result)
                else:
                    st.session_state.parsed = (None, None, None)

                st.success("✅ Article Generated")

# -------------------------------
# Display Results
# -------------------------------
if st.session_state.result:

    result = st.session_state.result
    html_content, css_content, js_content = st.session_state.parsed

    if generate_website:
        tabs = st.tabs(["📄 Article", "🌐 Preview", "💻 Code", "📥 Download"])
    else:
        tabs = st.tabs(["📄 Article", "📥 Download"])

    # -------------------------------
    # Article
    # -------------------------------
    with tabs[0]:
        st.subheader("📄 Article")
        stream_text(clean_article(result))

    # -------------------------------
    # Website
    # -------------------------------
    if generate_website:

        with tabs[1]:
            st.subheader("🌐 Live Preview")

            if html_content:
                full_page = f"""
                <style>{css_content}</style>
                {html_content}
                <script>{js_content}</script>
                """
                st.components.v1.html(full_page, height=500, scrolling=True)
            else:
                st.info("⚠️ Website not generated")

        with tabs[2]:
            st.subheader("💻 Code")

            if html_content:
                st.code(html_content, language="html")
                st.code(css_content, language="css")
                st.code(js_content, language="javascript")
            else:
                st.info("No code available")

    # -------------------------------
    # Download
    # -------------------------------
    download_tab_index = 3 if generate_website else 1

    with tabs[download_tab_index]:
        st.subheader("📥 Download")

        pdf_file = create_pdf(result)
        st.download_button("📄 Download PDF", pdf_file, "article.pdf")

        if generate_website and html_content:
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zipf:
                zipf.writestr("index.html", html_content)
                if css_content:
                    zipf.writestr("style.css", css_content)
                if js_content:
                    zipf.writestr("script.js", js_content)

            zip_buffer.seek(0)

            st.download_button("🌐 Download Website ZIP", zip_buffer, "website.zip")