import requests

c = requests.get("http://httpbin.org/json")

if c.status_code == 200:
	print(c.json())
else:
		print("Error")

