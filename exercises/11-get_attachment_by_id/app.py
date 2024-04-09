import requests

def get_attachment_by_id(attachment_id):
    # your code here
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    json = response.json()['posts']
    for post in json:
        for at in post['attachment']:
            if at ['id'] == attachment_id:
                at_r = at
                break
            else:
                at_r = None 
    return at_r

print(get_attachment_by_id(137))