import requests

# your code here

response = requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php')

print(response.json()[1]['name'])