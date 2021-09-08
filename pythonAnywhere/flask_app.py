# A very simple Flask Hello World app for you to get started with...
# Published in pythonanywhere

from flask import Flask
from flask import request
from flask_cors import CORS
from pa_carro_api import carros_api
from pa_emp_api import empdb_api
from pa_paraio_api import paraio_api
from global_ import Global

LOCAL = True
glb = Global()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(carros_api, url_prefix='/pstgr')
app.register_blueprint(empdb_api, url_prefix='/empdb') 
app.register_blueprint(paraio_api, url_prefix='/paraio') 


@app.route('/')
def hello_world():
    url_get = request.url
    print('URL:',url_get)
    print('IsLocal? ',glb.isLocal(request.url))
    return 'Hello from Flask!'

# IMPORTANTE: Para DEPLOY no pythonanywhere.com COMENTAR AS LINHAS ABAIXO
#if __name__ == '__main__':
#if LOCAL:
#    app.run()