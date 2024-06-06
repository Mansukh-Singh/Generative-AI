from langchain.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.llm import LLMChain
from langchain.prompts.chat import (ChatPromptTemplate,
                                    SystemMessagePromptTemplate,
                                    HumanMessagePromptTemplate,
                                    AIMessagePromptTemplate)
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate(
    input_variables = ["human_message"],
    messages = [
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant, you have to correct the code provided by the user"
        ),
        HumanMessagePromptTemplate.from_template(
            "Question : {human_message}"
        )
    ]
)

llm = Ollama(model = "llama2")

chain = LLMChain(
    llm = llm,
    prompt = prompt,
    output_parser = StrOutputParser()
)

st.title("Langchain Chatbot")
input_text = st.text_input("Enter your query")

if input_text:
    st.write(chain.invoke({"human_message":input_text}))
