import requests

session = requests.Session()
session.headers.update({'AccessToken':'ALOC-fa77c5b56cc4a7ba95d9'})
response = session.get('https://question.aloc.com.ng/api/v2/m?', params = {'subject': 'english', 'type': 'utme'})

response = response.json()
print(response)