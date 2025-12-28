import streamlit as st
from Bengaluru_backend import rag_chain
from bengaluru_references import REFERENCE_DB
from bengaluru_guard import detect_topic, bengaluru_guard
# Wikipedia-based RAG only

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Bengaluru AI 📘",
    page_icon="📘",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS (KNOWLEDGE THEME)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #f4f6f8;
}
.main {
    background-color: #f4f6f8;
}
h1 {
    color: #1f3c88;
    text-align: center;
    font-size: 3em;
}
h3 {
    color: #4a4a4a;
    text-align: center;
}
.subtext {
    text-align: center;
    color: #6c757d;
    font-size: 16px;
    margin-bottom: 25px;
}
.chat-box {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    margin-top: 20px;
}
.user {
    color: #1f3c88;
    font-weight: bold;
}
.bot {
    color: #333333;
}
input {
    border-radius: 10px;
}
.stButton>button {
    background-color: #1f3c88;
    color: #ffffff;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #162c66;
}
.footer {
    text-align: center;
    color: #6c757d;
    margin-top: 40px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<h1>📘 Bengaluru AI</h1>", unsafe_allow_html=True)
st.markdown("<h3>Learn about Bengaluru from Verified Wikipedia Sources</h3>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtext'>• History • Geography • Culture • Economy • Demographics • Tourism</p>",
    unsafe_allow_html=True
)

# -----------------------------
# INPUT
# -----------------------------
question = st.text_input(
    "Ask about Bengaluru (e.g., 'History of Bengaluru', 'Climate of Bengaluru')"
)

# -----------------------------
# BUTTON ACTION
# -----------------------------
if st.button("Get Information 🔍"):
    if question.strip() == "":
        st.warning("Please enter a question about Bengaluru.")
    elif not bengaluru_guard(question):
        st.error("❌ I don't know. This app only answers questions about Bengaluru.")
    else:
        with st.spinner("Searching Wikipedia knowledge... 📚"):
            answer = rag_chain(question)

        if answer is None or answer.lower().startswith("i don't know"):
            st.info("ℹ️ The answer was not found in Wikipedia sources.")
        else:
            st.markdown(f"<p class='user'>Question:</p> {question}", unsafe_allow_html=True)
            st.markdown(f"<p class='bot'>Answer:</p> {answer}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# REFERENCES
# -----------------------------
topic = detect_topic(question)

if topic and topic in REFERENCE_DB:
    refs = REFERENCE_DB[topic]

    # Websites
    if refs["websites"]:
        st.subheader("🔗 Reference Links")
        for site in refs["websites"]:
            for url in site['urls']:
                st.markdown(f"- [{site['title']}]({url})")

    # YouTube
    if refs["youtube"]:
        st.subheader("🎥 YouTube Videos")
        for vid in refs["youtube"]:
            st.video(vid["url"])

    # Images
    if refs["images"]:
        st.subheader("🖼️ Images")
        st.image(refs["images"])

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    "<div class='footer'>Powered by Wikipedia + RAG | Bengaluru Knowledge Assistant</div>",
    unsafe_allow_html=True
)
