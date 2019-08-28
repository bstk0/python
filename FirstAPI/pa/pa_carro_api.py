# A very simple Flask Hello World app for you to get started with...
# Published in pythonanywhere
import MySQLdb
from flask import Blueprint
from flask import jsonify

LOCAL = True

carros_api = Blueprint('carros_api', __name__)

#con = psycopg2.connect(database="xmkvsriw", user="xmkvsriw", password="0HlF-y1j5NUUszyn-2PqhgfJ-SJPPyWL", 
#                       host="elmer.db.elephantsql.com", port="5432")

if LOCAL:
    #pa config
    c_host="remotemysql.com"
    c_user="LWLzrEdTDm"
    c_passwd="ITvIPODqmC"
    c_database="LWLzrEdTDm"
else:    
    #pa config
    c_host="bisterco.mysql.pythonanywhere-services.com"
    c_user="bisterco"
    c_passwd="cobradb1"
    c_database="bisterco$db1"


con = MySQLdb.connect(
  host = c_host,
  user = c_user,
  passwd = c_passwd,
  database = c_database
)

@carros_api.route("/carros") 
def getAllCarros():
    cur = con.cursor()
    cur.execute("SELECT id, nome, modelo, ano, fabricante from carros")
    rows = cur.fetchall()

    #for row in rows:
    #    print("id =", row[0])
    #    print("Nome =", row[1])
    #    print("Modelo =", row[2])
    #    print("Ano =", row[3])
    #    print("Fabricante =", row[4], "\n")
    #con.close()
    return jsonify({'emps':rows})

# Importante: Para o pythonanywhere.com comentar as linhas abaixo
#if __name__ == '__main__':
#    app.run()