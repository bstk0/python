import requests
from flask import Blueprint
from flask import jsonify
#from global_ import Global

#LOCAL = True
#glb = Global()

paraio_api = Blueprint('paraio_api', __name__)

@paraio_api.route("/movim") 
def buscar_dados_movim():
    
    auth = {'Authorization' : 'Anonymous app:dbapp' }    
    request = requests.get("http://paraio.com/v1/movims?sort=timestamp&limit=10",headers=auth);
    #print(request.content);
    return jsonify(request.content)
    
#if __name__ == '__main__':
#    buscar_dados_movim()
    
    