# A very simple Flask Hello World app for you to get started with...
# Published in pythonanywhere

from flask import Flask
from flask import request
from pa_carro_api import carros_api
from pa_emp_api import empdb_api
#import global

LOCAL = True

app = Flask(__name__)

app.register_blueprint(carros_api, url_prefix='/pstgr')
app.register_blueprint(empdb_api, url_prefix='/empdb') 


@app.route('/')
def hello_world():
    url_get = request.url
    print('URL:',url_get)
    #global.
    return 'Hello from Flask!'

# Importante: Para o pythonanywhere.com comentar as linhas abaixo
#if __name__ == '__main__':
if LOCAL:
    app.run()