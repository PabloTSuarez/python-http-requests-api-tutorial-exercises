import requests

def get_post_tags(post_id):
    # your code here
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    json = response.json()['posts']
    for post in json:
        if post['id'] == post_id:
            tags = post['tags']
            break
        else:
            tags = None

    return tags

print(get_post_tags(146))