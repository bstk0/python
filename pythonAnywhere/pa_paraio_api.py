import requests
from flask import request
from flask import Blueprint
from flask import jsonify
#from global_ import Global

#LOCAL = True
#glb = Global()

paraio_api = Blueprint('paraio_api', __name__)

@paraio_api.route("/movim") 
def buscar_dados_movim():
    dias = request.args.get('dias', default='10', type = str)
    auth = {'Authorization' : 'Anonymous app:dbapp' }    
    returnRequest = requests.get("http://paraio.com/v1/movims?sort=timestamp&limit="+dias ,headers=auth);
    #print(request.content);
    #return jsonify(request.content)
    return returnRequest.content
    
    
@paraio_api.route("/saldo") 
def buscar_dados_saldo():
    
    auth = {'Authorization' : 'Anonymous app:dbapp' }    
    request = requests.get("https://paraio.com/v1/saldo/1143180213983645696",headers=auth);
    #print(request.content);
    #return jsonify(request.content)
    return request.content
    
#if __name__ == '__main__':
#    buscar_dados_movim()
    