import requests
responce = requests.get("https://fake-json-api.mock.beeceptor.com/users")
print(responce.status_code)