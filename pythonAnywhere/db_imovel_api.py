#
import requests
from flask import Blueprint
from flask import jsonify
#from flask import request
#from flask import abort

#LOCAL = True
#glb = Global()

imovel_api = Blueprint('imovel_api', __name__)

@imovel_api.route("/imovel", methods=['GET']) 
def buscar_dados_imovel():
    # dias = request.args.get('dias', default='10', type = str)
    # auth = {'Authorization' : 'Anonymous app:dbapp' }    
    # returnRequest = requests.get("http://paraio.com/v1/movims?sort=timestamp&limit="+dias ,headers=auth);
    # #print(request.content);
    # #return jsonify(request.content)
    # return returnRequest.content
    
    data = {
    "dataSource": "Cluster0",
    "database": "dbe",
    "collection": "imovel",
    "sort": { "nome" : 1} }
    
    #data = jsonify(data_text);

    #data = request.get_json();
    auth = {'api-key' : 'Cnf5kpOdWfE5oAJ5vTGoddZ0ZNI7acYh6G8sfAP6xye2imMfKKf1TMM5gQ35Six3' }    
    r = requests.post("https://data.mongodb-api.com/app/data-plfzo/endpoint/data/beta/action/find",json=data  ,headers=auth);
    #print(request.content);
    #return jsonify(request.content)
    #return str(r.status_code)
    return r.content



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
    