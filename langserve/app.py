from fastapi import FastAPI
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import (
    SystemMessagePromptTemplate ,
    HumanMessagePromptTemplate ,
    AIMessagePromptTemplate ,
    ChatPromptTemplate
)
from langserve import add_routes 
import uvicorn 


# OLLAMA - USE OS MODELS - setup
llm_engine = ChatOllama(
    model="deepseek-r1:1.5b", )


# system_prompt = SystemMessagePromptTemplate(" You are an expert in the field of performing testing in software,You write clear and concise test plans ")
prompt = ChatPromptTemplate.from_template("You are an expert in the field of performing testing in software,You write clear and concise test plans given : {topic}")
prompt2 = ChatPromptTemplate.from_template("Provide poems on the theme:{topic}")

app = FastAPI(
    title = "Langchain server", 
    version = "1.0",
    description = "A beginner level server"
)

# ADD ROUTES 
# generic deepseek
add_routes(
    app , 
    ChatOllama(),
    path = "/ollama"
)

# tester deepseek
add_routes(
    app , 
    prompt | llm_engine,
    path ="/tester"

)

# artist deepseek
add_routes(
    app , 
    prompt2 | llm_engine,
    path ="/artist")


if __name__ == "__main__":
    uvicorn.run(app,host ="localhost",port =8000)


