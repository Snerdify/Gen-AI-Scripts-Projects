'''
Pseudo-Code


from openai import OpenAI 
from pydantic import BaseModel, Field 
import json

client= OpenAI(api_key="sk-abcdqrstefgh5678abcdqrstefgh5678abcdqrst")
MODEL ="gpt-4o-2024-08-06"

query="""
Hi , I am having trouble tracking my order . Can you help me with my tracking process?
"""

system_prompt = """
You are an AI customer care assistant. You will be provided with a customer query , 
and your goal is to respond with a structured solution, include the steps needed to resolve the issue.
And for each step provide a description and the action taken
 """


class X(BaseModel):
    class Step(BaseModel):
        description: str = Field(description="Description of the steps taken")
        action: str = Field(action="Action taken to solve the issue")

    steps: list[Step]
    final_answer : str = Field(description="Final answer given to the user")
    confidence:float = Field(description="Confidence level of the answer (0-1)", ge=0 ,le=1)


    def func(query:str):
        completion = client.beta.chat.completions.parse(
        model = MODEL,
        messages=["role":"system" , "content" :"system_prompt"],
        {"role":"user", "content":query},)
        response_format= X,
        )

    return completion[0].message.parsed

response_pydantic = func(query)
response_pydantic.model_dump()
'''