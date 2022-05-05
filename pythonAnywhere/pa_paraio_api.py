import requests
from flask import request
from flask import Blueprint
from flask import jsonify
#from global_ import Global

#LOCAL = True
#glb = Global()

paraio_api = Blueprint('paraio_api', __name__)

@paraio_api.route("/movim", methods=['GET']) 
def buscar_dados_movim():
    dias = request.args.get('dias', default='10', type = str)
    auth = {'Authorization' : 'Anonymous app:dbapp' }    
    returnRequest = requests.get("http://paraio.com/v1/movims?sort=timestamp&limit="+dias ,headers=auth);
    #print(request.content);
    #return jsonify(request.content)
    return returnRequest.content

@paraio_api.route("/movim", methods=['POST']) 
def insert_dados_movim():
    data = request.get_json();
    auth = {'Authorization' : 'Anonymous app:dbapp','Content-Type' : 'application/json' }    
    returnRequest = requests.post("https://paraio.com/v1/movims/", json=data, headers=auth, verify=False);
    #print(request.content);
    #return jsonify(request.content)
    return str(returnRequest.status_code)

    
@paraio_api.route("/saldo", methods=['GET']) 
def buscar_dados_saldo():
    
    auth = {'Authorization' : 'Anonymous app:dbapp' }    
    # NOVO - 1433168973335105536 / ANTES: 1143180213983645696
    request = requests.get("https://paraio.com/v1/saldo/1433168973305745408",headers=auth);
    #print(request.content);
    #return jsonify(request.content)
    return request.content

@paraio_api.route("/saldo", methods=['PUT']) 
def update_saldo():
    data = request.get_json();
    auth = {'Authorization' : 'Anonymous app:dbapp' }    
    # NOVO - 1433168973305745408 / ANTES: 1143180213983645696
    r = requests.put("https://paraio.com/v1/saldo/1433168973305745408",json=data  ,headers=auth);
    #print(request.content);
    #return jsonify(request.content)
    return str(r.status_code)



#if __name__ == '__main__':
#    buscar_dados_movim()
    