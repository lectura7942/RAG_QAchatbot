import streamlit as st
from utils import get_rag_chain

rag_chain = get_rag_chain()

st.title("📝 PDF 기반 QA 챗봇")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "질문에 답변해드립니다."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = st.chat_message("assistant").write_stream(rag_chain.stream(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})
