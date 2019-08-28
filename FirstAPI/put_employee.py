import requests

url = "http://bisterco.pythonanywhere.com/empdb/employee/101"

#payload = "{\"field2\":\"new value\"}"

employee = "{\"name\":\"Ze da Silva\"}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("PUT", url, data=employee, headers=headers)

print(response.text)