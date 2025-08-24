import streamlit as st

st.title("Zuban-e-Kisan Chatbot")
st.caption("Prototype chatbot module for Zuban-e-Kisan — bridging farmers and technology through conversational support.")


if 'message_history' not in st.session_state:
    st.session_state.message_history = []

for message in st.session_state.message_history:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.text(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.text(message["content"])

userInput = st.chat_input("Type your message here...")
if userInput:
    st.session_state.message_history.append({"role": "user", "content": userInput})
    with st.chat_message("user"):
        st.text(userInput)
    st.session_state.message_history.append({"role": "assistant", "content": "..."})
    with st.chat_message("assistant"):
        st.markdown("...")