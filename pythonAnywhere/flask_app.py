# A very simple Flask Hello World app for you to get started with...
# Published in pythonanywhere

from flask import Flask
from flask import request
from pa_carro_api import carros_api
from pa_emp_api import empdb_api
from global_ import Global

LOCAL = True
glb = Global()

app = Flask(__name__)

app.register_blueprint(carros_api, url_prefix='/pstgr')
app.register_blueprint(empdb_api, url_prefix='/empdb') 


@app.route('/')
def hello_world():
    url_get = request.url
    print('URL:',url_get)
    print('IsLocal? ',glb.isLocal(request.url))
    return 'Hello from Flask!'

# Importante: Para o pythonanywhere.com comentar as linhas abaixo
#if __name__ == '__main__':
if LOCAL:
    app.run()