
import requests

api_url = "https://dog.ceo/api/breeds/list/all"

params = {"count": 10}
response = requests.get(api_url, params=params)

status_code = response.status_code
print("status code: ", status_code)

response_json = response.json()
print(response_json)
print(response.url)