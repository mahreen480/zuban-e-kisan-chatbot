import streamlit as st
from Backend import graph as chatbot, HumanMessage

st.set_page_config(page_title="Zuban-e-Kisan Chatbot", page_icon="👨‍🌾", layout="wide")

st.title("👨‍🌾 Zuban-e-Kisan Chatbot")
st.caption("Prototype chatbot module for Zuban-e-Kisan — bridging farmers and technology through conversational support.")

CONFIG = {
    'configurable':{
        'thread_id': 1
    }
}

if "message_history" not in st.session_state:
    st.session_state.message_history = []

for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

userInput = st.chat_input("Type your message here...")
if userInput:
    st.session_state.message_history.append({"role": "user", "content": userInput})
    with st.chat_message("user"):
        st.markdown(userInput)

    with st.chat_message("assistant"):
        response = st.write_stream(
            message_chunk.content for message_chunk, meta_data in chatbot.stream(
            { "messages": [HumanMessage(content=userInput)]},
            config=CONFIG,
            stream_mode='messages'
        ))
    st.session_state.message_history.append({"role": "assistant", "content": response})
