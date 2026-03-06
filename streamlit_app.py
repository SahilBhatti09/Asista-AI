"""
Streamlit frontend for the chatbot. Kept separate from chatbot logic.
Run from repo root: streamlit run chatmodel/streamlit_app.py
"""
import random
import streamlit as st

from chatbot_app import get_response

st.set_page_config(page_title="Chatbot", layout="centered")
# st.title("Asista AI")

st.markdown(
    "<h1 style='text-align: center'>Asista AI</h1>",
    unsafe_allow_html=True )

welcome = ['Your AI assistant is ready to help you!','How can I help you today?', 'what can I do for you?', 'how can I assist you?', 'let\'s dive in!']
random_welcome = random.choice(welcome)

# st.write(random_welcome)
st.markdown(
    "<p style='text-align: center'>{}</p>".format(random_welcome),
    unsafe_allow_html=True
)


if "messages" not in st.session_state:
    st.session_state.messages = []

for i, msg in enumerate(st.session_state.messages):
    role = "user" if i % 2 == 0 else "assistant"
    with st.chat_message(role):
        st.write(msg)

if prompt := st.chat_input("Your message"):
    st.session_state.messages.append(prompt)

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_response(st.session_state.messages)
        st.session_state.messages.append(reply)
        st.write(reply)
