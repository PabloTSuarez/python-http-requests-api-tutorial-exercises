import requests

def get_titles():
    # your code here
    titles = []
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    for resp in response.json()['posts']:
        titles.append(resp['title'])
    return titles

print(get_titles())


