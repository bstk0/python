import json
import requests

'''
Consumindo API do github - teste meu usuario:
https://api.github.com/users/bstk0
'''
api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'Python Student',
           'Accept': 'application/vnd.github.v3+json'}

def get_repos(username):

    api_url = '{}users/{}'.format(api_url_base, username)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return (response.content)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

repo_list = get_repos('bstk0')

if repo_list is not None:
    print(repo_list)
    y = json.loads(repo_list)
    # the result is a Python dictionary:
    print("login:",y["login"])
    print("url:",y["url"])
else:
    print('No Repo List Found')    