# A very simple Flask Hello World app for you to get started with...
# Published in pythonanywhere

from flask import Flask,abort
from flask import jsonify
from flask import request
import psycopg2

app = Flask(__name__)

"""
empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]
""" 

con = psycopg2.connect(database="xmkvsriw", user="xmkvsriw", password="0HlF-y1j5NUUszyn-2PqhgfJ-SJPPyWL", 
                       host="elmer.db.elephantsql.com", port="5432")

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'


@app.route('/pstgr/carros',methods=['GET'])
def getAllCarros():
    cur = con.cursor()
    cur.execute("SELECT id, nome, modelo, ano, fabricante from carros")
    rows = cur.fetchall()

    for row in rows:
        print("id =", row[0])
        print("Nome =", row[1])
        print("Modelo =", row[2])
        print("Ano =", row[3])
        print("Fabricante =", row[4], "\n")
    
    return jsonify({'emps':rows})

# Importante: Para o pythonanywhere.com comentar as linhas abaixo
#if __name__ == '__main__':
#    app.run()