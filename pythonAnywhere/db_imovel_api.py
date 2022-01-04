#
import requests
import json
from flask import Blueprint
#from flask import jsonify
#from flask import request
#from flask import abort

#LOCAL = True
#glb = Global()

imovel_api = Blueprint('imovel_api', __name__)

@imovel_api.route("/imovel", methods=['GET']) 
def buscar_dados_imovel():
    url = "https://data.mongodb-api.com/app/data-plfzo/endpoint/data/beta/action/find"
    
    payload = json.dumps({
      "dataSource": "Cluster0",
      "database": "dbe",
      "collection": "imovel",
      "sort": {
        "nome": 1
      }
    })
    
    headers = {
      'api-key': 'Cnf5kpOdWfE5oAJ5vTGoddZ0ZNI7acYh6G8sfAP6xye2imMfKKf1TMM5gQ35Six3',
      'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    #print(response.text)    
    #return r.content
    return response.text


# @paraio_api.route("/movim", methods=['POST']) 
# def insert_dados_movim():
#     data = request.get_json();
#     auth = {'Authorization' : 'Anonymous app:dbapp','Content-Type' : 'application/json' }    
#     returnRequest = requests.post("https://paraio.com/v1/movims/", json=data, headers=auth, verify=False);
#     #print(request.content);
#     #return jsonify(request.content)
#     return str(returnRequest.status_code)
#
#
# @paraio_api.route("/saldo", methods=['GET']) 
# def buscar_dados_saldo():
#
#     auth = {'Authorization' : 'Anonymous app:dbapp' }    
#     request = requests.get("https://paraio.com/v1/saldo/1143180213983645696",headers=auth);
#     #print(request.content);
#     #return jsonify(request.content)
#     return request.content
#
# @paraio_api.route("/saldo", methods=['PUT']) 
# def update_saldo():
#     data = request.get_json();
#     auth = {'Authorization' : 'Anonymous app:dbapp' }    
#     r = requests.put("https://paraio.com/v1/saldo/1143180213983645696",json=data  ,headers=auth);
#     #print(request.content);
#     #return jsonify(request.content)
#     return str(r.status_code)



#if __name__ == '__main__':
#    buscar_dados_movim()
    