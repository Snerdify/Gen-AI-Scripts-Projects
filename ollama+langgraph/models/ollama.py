import requests
import json
import ast


# seperate the model component from the agent component 
# model - do all the things to use llm based service -ollama , mistral claude 

# general pattern - model - endpoint , data , format of data , passing the response for that data 
# 2 classes - one for working with json and another for working with text generation 


class OllamaJsonModel:
    # initiate the class with the ollama endpoint
    def __init__(self ,temperature=0 , model="llama2"):
        self.headers = {}
        self.endpoint = " "
        self.temperature = temperature
        self.model = model
        
    def invoke(self, messages):
        system = messages[0]["content"]
        user = messages[1]["content"]
        # post data to the endpoint
        payload ={
            "model" : self.model ,
            "system": system , 
            "stream": False, 
            "temperature": 0,
              
        }

        pass 



class OllamaModel:
    def __init__( )