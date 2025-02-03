import requests

response  = requests.post("http://localhost:8000/tester/invoke",
                         json ={'input':{'topic' :"unit testing"}})

print(response.json()['output']['content'])
