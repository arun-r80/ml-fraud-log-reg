from flask import Flask
from flask import jsonify
from flask import request
from predictor import predict_fraudulent_singleentry
from config_model import CONFIG
app = Flask(__name__)
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
@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})
@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    PRIMARYPROCEDURECODENO=request.args.get('PRIMARYPROCEDURECODENO')
    MEMBERGENDERNO=request.args.get('MEMBERGENDERNO')

    
    c=predict_fraudulent_singleentry(
            MEMBERGENDERNO,
            PRIMARYPROCEDURECODENO
            )
                                        
    #usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':c})
@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json : 
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    return jsonify({'emp':em[0]})
@app.route('/empdb/employee',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)
@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
       abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
if __name__ == '__main__':
 app.run()