# 🛡️ PhemSentinel – AI-Powered Linux Log Analyzer

**PhemSentinel** is a smart, open-source cybersecurity tool that helps you analyze `auth.log` files for brute-force attacks and suspicious login activity.  
It also leverages **AI** to explain log entries in plain English — ideal for learners, SOC analysts, and sysadmins.

> 🔧 Built with: Python · Streamlit · OpenRouter API


## 🚀 Features

- 📂 Upload Linux `auth.log` or `.txt` files  
- 🔍 Detect brute-force SSH attacks and failed logins  
- 🧠 AI-powered explanation of log entries (via OpenRouter)  
- 📜 View raw log entries and AI interpretation  
- ✅ Built-in risk assessment  
- 🧑‍💻 Designed and built by [**Ajijola Oluwafemi Blessing**](https://www.linkedin.com/in/...)


## 🌐 Live Demo

👉 Try it here:  
[https://phemsentinel-c8zukqm5egllzqv6fswgj4.streamlit.app](https://phemsentinel-c8zukqm5egllzqv6fswgj4.streamlit.app)


## 🧠 How the AI Works

PhemSentinel uses OpenRouter’s LLMs (like Mistral) to convert cryptic log lines like:

```log
Failed password for invalid user root from 192.168.1.10 port 42122 ssh2
```

Into understandable English:

```text
"This indicates a failed SSH login attempt for the root user from IP 192.168.1.10 — possibly a brute-force attack."
```

## ⚙️ Local Setup

```bash
# Clone the repository
git clone https://github.com/phemtech-solutions/PhemSentinel.git
cd PhemSentinel

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create your API key file:

```toml
# .streamlit/secrets.toml
OPENROUTER_API_KEY = "your-openrouter-api-key-here"
```

Run the app:

```bash
streamlit run app.py
```

## 📁 Project Structure

```plaintext
PhemSentinel/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── utils/
│   ├── ai.py               # OpenRouter API logic
│   └── parser.py           # Log parsing and analysis
└── .streamlit/
    └── secrets.toml        # API key (excluded from Git)
```


## 👨‍💻 Author

**Ajijola Oluwafemi Blessing**  
Cybersecurity | Software | IT | Research

- GitHub: [phemtech-solutions](https://github.com/oluwafemiab/ajijola.github.io)  
- LinkedIn: [https://www.linkedin.com/in/ajijola-oluwafemi-ba839712a/)

