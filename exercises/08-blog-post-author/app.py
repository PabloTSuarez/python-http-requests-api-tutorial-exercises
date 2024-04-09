import requests

# your code here

response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')

print(response.json()['posts'][0]['author']['name'])