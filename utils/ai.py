import requests
import streamlit as st

def explain_log_line(log_line):
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": "You are a cybersecurity expert that explains Linux log lines clearly and simply."},
                {"role": "user", "content": f"Explain this log line: {log_line}"}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"❌ API Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
