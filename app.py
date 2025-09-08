import streamlit as st
import requests
import base64

# ---------------------------
# Initialize session state
# ---------------------------
if "word_count" not in st.session_state:
    st.session_state["word_count"] = 0

if "summary" not in st.session_state:
    st.session_state["summary"] = ""

if "readability_score" not in st.session_state:   # ✅ new
    st.session_state["readability_score"] = 0

if "history" not in st.session_state:   # ✅ new
    st.session_state["history"] = []

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="AI Text Summarizer", layout="wide")

# ---------------------------
# Function to set background
# ---------------------------
def set_bg_image(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Heading Style */
        h1 {{
            font-family: 'Russo One', sans-serif;
            color: black;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            text-align: center;
            font-size: 48px;
            font-style: italic;      /* Slanted heading */
            margin-bottom: 40px;     /* Space below heading */
        }}

        /* Subheader Style */
        h2 {{
            font-family: 'Russo One', sans-serif;
            color: black;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }}

        /* Button Style */
        .stButton > button {{
            background-color: #8E8E8E;
            color: white ! important;
            border: none;
            border-radius: 20px;
            padding: 14px 36px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease-in-out;
        }}
        .stButton > button:hover {{
            background-color: #7A7A7A;
            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.35);
            transform: scale(1.05);
        }}
        </style>

        <!-- Google Font -->
        <link href="https://fonts.googleapis.com/css2?family=Russo+One&display=swap" rel="stylesheet">
        """,
        unsafe_allow_html=True
    )

# Set the background
set_bg_image("background.jpg")

# ---------------------------
# App Title
# ---------------------------
st.title("📄 AI Text Summarizer")

# ---------------------------
# Layout: Input (Left) | Output (Right)
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Paste your text here")
    user_input = st.text_area("Input Text", height=300, label_visibility="collapsed")

    if st.button("Summarize"):
        if user_input.strip():
            try:
                response = requests.post(
                    "http://127.0.0.1:5000/summarize",
                    json={"text": user_input}
                )
                if response.status_code == 200:
                    result = response.json()
                    st.session_state["summary"] = result.get("summary", "")
                    st.session_state["word_count"] = result.get("word_count", 0)
                    st.session_state["readability_score"] = result.get("readability_score", 0)

                    # ✅ Save to history
                    st.session_state["history"].append({
                        "input": user_input,
                        "summary": st.session_state["summary"],
                        "word_count": st.session_state["word_count"],
                        "readability": st.session_state["readability_score"]
                    })
                else:
                    st.error("❌ Backend error: Unable to generate summary")
            except Exception as e:
                st.error(f"⚠️ Error connecting to backend: {e}")
        else:
            st.warning("⚠️ Please enter some text to summarize.")

with col2:
    st.subheader("Summary Output")
    st.text_area("Summary", value=st.session_state["summary"], height=300, label_visibility="collapsed")
    st.write(f"**Word Count:** {st.session_state['word_count']}")
    st.write(f"**Readability Score:** {st.session_state['readability_score']:.2f}")   # ✅ new

# ---------------------------
# History Section
# ---------------------------
st.subheader("History of Summaries")
for i, entry in enumerate(st.session_state["history"], 1):
    with st.expander(f"Summary {i} (Words: {entry['word_count']}, Readability: {entry['readability']:.2f})"):
        st.write("**Original Text:**")
        st.write(entry["input"])
        st.write("**Summary:**")
        st.write(entry["summary"])






