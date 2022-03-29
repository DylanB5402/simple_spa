import requests

# http://127.0.0.1:5000/
print(requests.get("http://127.0.0.1:5000/").text)
print(requests.post("http://127.0.0.1:5000/login").text)