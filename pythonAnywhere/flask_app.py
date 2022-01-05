# A very simple Flask Hello World app for you to get started with...
# Published in pythonanywhere
import os
from flask import Flask
from flask import request
from flask_cors import CORS
#from flask_restplus import abort
#from functools import wraps
from pa_carro_api import carros_api
from pa_emp_api import empdb_api
from pa_paraio_api import paraio_api
from db_imovel_api import imovel_api
from global_ import Global

LOCAL = True
glb = Global()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app)

app.register_blueprint(carros_api, url_prefix='/pstgr')
app.register_blueprint(empdb_api, url_prefix='/empdb') 
app.register_blueprint(paraio_api, url_prefix='/paraio')
app.register_blueprint(imovel_api, url_prefix='/mongo') 

@app.route('/')
def hello_world():
    url_get = request.url
    print('URL:',url_get)
    print('IsLocal? ',glb.isLocal(request.url))
    return 'Hello from Flask!'

# # decorator security
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#
#         token = request.headers.get('AUTH-TOKEN')
#         if not token:
#             abort(401, 'Authentication token is missing')
#
#         if token != os.getenv('API_KEY'):
#             abort(401, 'Authentication token is wrong')
#
#         # try:
#         #     user = auth.validate_token(token)
#         # except SignatureExpired as e:
#         #     abort(401, e.message)
#         # except BadSignature as e:
#         #     abort(401, e.message)
#
#         return f(*args, **kwargs)
#     return decorated


# IMPORTANTE: Para DEPLOY no pythonanywhere.com COMENTAR AS LINHAS ABAIXO
#if __name__ == '__main__':
#if LOCAL:
#    app.run()