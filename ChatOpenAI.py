from langchain.chat_models.openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import (ChatPromptTemplate,
                               SystemMessagePromptTemplate,
                               HumanMessagePromptTemplate,
                               AIMessagePromptTemplate)
from langchain.chains.llm import LLMChain  
import streamlit as st                             
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate(
    input_variables = ["human_message"],
    messages = [
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant, please respond to the user queries"
        ),
        HumanMessagePromptTemplate.from_template(
            "Question : {human_message}"
        )
    ]
)

llm = ChatOpenAI(model = "gpt-3.5-turbo")

chain = LLMChain(
    llm = llm,
    prompt = prompt,
    output_parser = StrOutputParser()
)

st.title("Langchain Chatbot")
input_text = st.text_input("Enter your query")

if input_text:
    st.write(chain.invoke({"human_message":input_text}))