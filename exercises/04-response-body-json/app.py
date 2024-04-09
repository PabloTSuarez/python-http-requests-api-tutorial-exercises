import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
#print(response.text)

dict = response.json()
#print(dict)

print(f"Current time: {dict['hours']} hrs {dict['minutes'] } min and {dict['seconds']} sec")