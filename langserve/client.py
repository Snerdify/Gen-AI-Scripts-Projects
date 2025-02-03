import requests

response  = requests.get("http://localhost:8000/tester/output_schema",
                         json ={'input':{'topic' :"unit testing"}})

print(response.json())
