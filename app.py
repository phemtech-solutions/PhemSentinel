import streamlit as st
from utils.ai import explain_log_line
from utils.parser import parse_auth_log

# Initialize session state if not already present
if "failed_logins" not in st.session_state:
    st.session_state.failed_logins = []

st.set_page_config(page_title="PhemSentinel", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .big-title {
            font-size: 2.5em;
            font-weight: bold;
        }
        .subtitle {
            font-size: 1.2em;
            color: gray;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            color: #888;
            font-size: 0.9em;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 PhemSentinel – AI-Powered Log Analyzer")
st.markdown('<div class="subtitle">Upload your Linux <code>auth.log</code> file to detect suspicious activity</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Upload your `auth.log` file", type=["log", "txt"])
log_text = None  # initialize variable

if uploaded_file is not None:
    try:
        log_text = uploaded_file.read().decode("utf-8", errors="ignore")
        st.success("✅ File uploaded successfully.")
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        log_text = None

# ANALYSIS SECTION
if log_text:
    if st.button("🔍 Analyze Log File"):
        st.info("Analyzing log file...")
        failed_logins, brute_summary = parse_auth_log(log_text)
        st.session_state.failed_logins = failed_logins  # Save to session

        st.write(f"🔍 Detected **{len(failed_logins)}** failed login attempts.")

        if brute_summary:
            st.warning("🚨 Brute force attempts detected:")
            for ip, count in brute_summary.items():
                st.markdown(f"- {ip}: **{count}** attempts")
        else:
            st.success("✅ No brute-force patterns detected.")

# SHOW ANALYSIS + AI if results exist
if st.session_state.failed_logins:
    with st.expander("📜 View Raw Failed Logins"):
        for ip, line in st.session_state.failed_logins:
            st.text(line)

    st.markdown("## 🧠 Explain a Log Line with AI")
    log_to_explain = st.selectbox(
        "Choose a log line to analyze:",
        [line for _, line in st.session_state.failed_logins],
        index=0
    )

    if st.button("Explain Log Line"):
        with st.spinner("Asking the AI..."):
            explanation = explain_log_line(log_to_explain)
            st.success("✅ Explanation:")
            st.markdown(explanation)
            st.code(explanation)

# Footer
st.markdown('<div class="footer">Designed by <b>Ajijola Oluwafemi Blessing</b></div>', unsafe_allow_html=True)
