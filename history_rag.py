import streamlit as st
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from utils import get_history_rag_chain

rag_chain = get_history_rag_chain()

history = StreamlitChatMessageHistory(key="test")

if len(history.messages) == 0 or st.sidebar.button("초기화"):
    history.clear()
    history.add_ai_message("문서 내용에 대해 질문하면 답변해드립니다.")


conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    # get_session_history,
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

for msg in history.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input():
    st.chat_message("human").write(prompt)

    # As usual, new messages are added to StreamlitChatMessageHistory when the Chain is called.
    config = {"configurable": {"session_id": "test"}}
    with st.spinner("답변 확인 중..."):
        response = conversational_rag_chain.invoke({"input": prompt}, config)
    st.chat_message("ai").write(response["answer"])
