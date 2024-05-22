import streamlit as st
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

with st.sidebar:
    model = st.selectbox("モデルを選択してください", [
        "gpt-4-turbo",
        "gpt-3.5-turbo",
    ])

st.title("OpenAI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if content := st.chat_input("入力してください"):
    st.chat_message("user").markdown(content)
    st.session_state.messages.append({
        "role": "user",
        "content": content,
    })

    # 過去6個のメッセージを含める
    past_messages = st.session_state.messages[-6:]

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "あなたは有能なアシスタントです"},
            *past_messages,
            {"role": "user", "content": content},
        ]
    )

    response = completion.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
    })
