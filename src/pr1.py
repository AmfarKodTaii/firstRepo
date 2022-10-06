import requests
URL="https://jsonplaceholder.typicode.com/users"
response=requests.get(URL)
print(response.text)
print(response.status_code)

123