import requests

url = "http://bisterco.pythonanywhere.com/empdb/employee"

headers = {
    'content-type': "application/json",
    'x-apikey': "560bd47058e7ab1b2648f4e7",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
