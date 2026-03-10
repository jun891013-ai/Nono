web: gunicorn --bind :$PORT main:app
import streamlit as st
import google.generativeai as genai

# 사이트 설정
st.set_page_config(page_title="나의 AI 서비스", page_icon="🤖")
st.title("안녕하세요! AI 서비스입니다")

# API 키 설정 (Streamlit 설정에서 넣을 거예요)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 간단한 채팅 창
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = model.generate_content(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.chat_message("assistant").write(response.text)

if __name__ == "__main__":
    import os
    # 반드시 0.0.0.0 이어야 합니다! 127.0.0.1은 안 돼요.
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

import os
from flask import Flask # 또는 사용하시는 프레임워크

app = Flask(__name__)