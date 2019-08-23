import requests

url = "http://bisterco.pythonanywhere.com/empdb/employee"

#payload = json.dumps( {"field1": "xyz","field2": "abc"} )

employee = "{\"id\":\"203\",\"name\":\"Rodrigo Bisterco 203\",\"title\":\"Technical Leader 203\"}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=employee, headers=headers)

print(response.text)