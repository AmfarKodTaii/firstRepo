import requests
URL="https://jsonplaceholder.typicode.com/users"
print("Search by username:")
user=input("> ")
queryUrl = URL + f"?username={user}"
response=requests.get(queryUrl)
print(response.text)
