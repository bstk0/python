# A very simple Flask Hello World app for you to get started with...
# Published in pythonanywhere

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import abort

empdb_api = Blueprint('empdb_api', __name__)

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

@empdb_api.route('/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@empdb_api.route('/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ]
    return jsonify({'emp':usr})

@empdb_api.route('/employee/<empId>',methods=['PUT'])
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    return jsonify({'emp':em[0]})

@empdb_api.route('/employee',methods=['POST'])
def createEmp():
    empLen = empDB.__len__()+1
    dat = {
    'id':str(empLen),
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@empdb_api.route('/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
        abort(404)

    empDB.remove(em[0])
    return jsonify({'response':'Success'})
