import streamlit as st
from Backend import chatbot

st.title("👨‍🌾 Zuban-e-Kisan Chatbot")
st.caption("Prototype chatbot module for Zuban-e-Kisan — bridging farmers and technology through conversational support.")

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
            chunk for chunk in chatbot.stream({
                'query': userInput
            })
        )
    st.session_state.message_history.append({"role": "assistant", "content": response})
