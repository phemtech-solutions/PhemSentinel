import streamlit as st
from utils.parser import parse_auth_log

st.set_page_config(page_title="PhemSentinel", layout="wide")

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

if uploaded_file is not None:
    try:
        log_text = uploaded_file.read().decode("utf-8", errors="ignore")  # More robust decoding
        st.success("✅ File uploaded successfully.")
        
        if st.button("🔍 Analyze Log File"):
            st.info("Analyzing log file...")
            failed_logins, brute_summary = parse_auth_log(log_text)

            st.write(f"🔍 Detected **{len(failed_logins)}** failed login attempts.")
            
            if brute_summary:
                st.warning("🚨 Brute force attempts detected:")
                for ip, count in brute_summary.items():
                    st.markdown(f"- {ip}: **{count}** attempts")
            else:
                st.success("✅ No brute-force patterns detected.")

            with st.expander("📜 View Raw Failed Logins"):
                for ip, line in failed_logins:
                    st.text(line)

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

st.markdown('<div class="footer">Designed by <b>Ajijola Oluwafemi Blessing</b></div>', unsafe_allow_html=True)
