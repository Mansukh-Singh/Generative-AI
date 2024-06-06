from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate,AIMessagePromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.llms.ollama import Ollama
from langserve import add_routes
import uvicorn
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = FastAPI()

chat_model = ChatOpenAI()
llm = Ollama()

prompt1 = ChatPromptTemplate.from_template(
        "Write an poem about {topic} in 100 words"
) 

prompt2 = ChatPromptTemplate.from_template(
    "Write an essay about {topic} in 100 words"
)

add_routes(
    app,
    prompt1|chat_model,
    path = "/essay"
)

add_routes(
    app,
    prompt2|llm,
    path = '/poem'
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)