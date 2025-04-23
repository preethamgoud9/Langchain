from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")
user_input = st.text_input("Enter Your Prompt")

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
