# create a customer care assistant that gives insights into a lot of metadata and reasoning behind AI 
# This is the second way to get structured outputs from a model ->
# Response Format: devs can supply a JSON SCHEMA via option json_schema in response_format parameter
# This is useful when a model is not calling a tool but responding to a user in a structured way 
# This method works with newer models : gpt-4o-2024-08-06 , gpt-4o-mini-2024-07-18

# When a response_format is provided with strict:True , then model output will match the supplied schema 




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

def get_response_json(query):
    response = client.chat.completions.create(
        model = MODEL ,
        messages = [\
            {"role":"system", "content":system_prompt},
            {"role":"user", "content":"query"},],
        response_format = {
            "type":"json_schema",
            "json_schema":{
                "name":"",
                "strict":True ,
                "schema":{
                    "type":"object",
                    "properties":{
                        "steps":{
                            "type":"array",
                            "items":{
                                "type":"object",
                                "properties":{
                                    "description":{
                                        "type":"string",
                                        "description":"Description of the steps taken"
                                    },
                                    "action":{
                                        "type":"string",
                                        "description":"Action taken to resolve the issue"
                                            },
                                    "required":["description","action"],
                                    "additional_properties": False,
                                }
                            },
                            "final_answer":{
                                "type":"string",
                                "description":"Final answer given to the user"
                            }
                        },
                        "required":["steps","final_answer"],
                        "additional_properties": False,


                    }

                },
                


            },
        },
    )

    return response.choices[0].message




response = get_response_json(query)

# below line gives params like-> content, refusal , role , function_call, tool_calls
# response.model_dump()

# to check if we are getting the json format
# gives the structured json output 
response_json = json.loads(response.content)

# use the above generated json data to run following steps 
for step in response_json["steps"]:
    print(f"Step:{step['description']}")
    print(f"Action:{step['action']}\n")

print(response_json["final_answer"])
    


