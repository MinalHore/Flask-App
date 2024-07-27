from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from pymongo import MongoClient
import json
from bson.objectid import ObjectId
from bson.json_util import dumps

app=Flask(__name__)
api=Api(app)

mongo_uri = "mongodb+srv://minalhore34:vyNMD5b4tyQntAKd@flaskcluster.27n5sf7.mongodb.net/?retryWrites=true&w=majority&appName=FlaskCluster"
client=MongoClient(mongo_uri)

db=client['Flask-DB']
collection=db['Employees']

# employees=[]
# employees={
#         "E001" : {"Name":"Pratik","Age":20,"Department":"IT"},
#         "E002" : {"Name":"Renu","Age":22,"Department":"HR"},
#         "E003" : {"Name":"Supriya","Age":18,"Department":"Finance"},
#         "E004" : {"Name":"Yash","Age":24,"Department":"Counsellor"},
# }

class EmployeeAPI(Resource):
    def get(self):
        # employees=list(collection.find({},{'_id':0}))
        employees=json.loads(dumps(collection.find({},{'_id':0})))        
        return employees,200

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument("ID",type=int,required=True,help='ID cannot be blank')
        parser.add_argument("Name",type=str,required=True,help='Name cannot be balnk')
        parser.add_argument("Age",type=int,required=True,help='Age cannot be balnk')
        parser.add_argument("Department",type=str,required=True,help='Department cannot be balnk')
        
        data=parser.parse_args()

        # for employee in employees:
            # if employee['ID']==data['ID']:
        if collection.find_one({'ID':data['ID']}):
                # return{'message':f"Employee with the name {data['ID']} already exists.!!!"},400
                 return{'message':f"Employees with the ID{data['ID']}already exists."},400
        new_employee={
            'ID':data['ID'],
            'Name':data['Name'],
            'Age':data['Age'],
            'Department':data['Department']
        }
        # employees.append(new_employee)
        # collection.insert_one(employees)
        result=collection.insert_one(new_employee)
        new_employee['_id']=str(result.inserted_id) 
        return new_employee,201


class SingleEmployeeAPI(Resource):
    def get(self,ID):
        # return employees[emp_id]
        employee=collection.find_one({'ID':int(ID)})
        if employee:
            employee['_id']=str(employee['_id'])
            return employee,200
        return{'message':'Employee not found'},404 


    def put(self,ID):
        data=request.get_json()
        employee=collection.find_one({'ID':int(ID)})
        if not employee:
            return{'message':'Employee not found'},404

        updated_employee={
            'Name':data['Name'],
            'Age':data['Age'],
            'Department':data['Department']
        }
        collection.update_one({'ID':int(ID)},{'$set':updated_employee})
        updated_employee['ID']=int(ID)
        return{'message':'Employee updated succcessfully'},200 

    def delete(self,ID):
        employee=collection.find_one({'ID':int(ID)})
        if employee:
            collection.delete_one({'ID':int(ID)})
            return {'message':'Employee deleted successfully'},200
        return{'message':'employee not found'},404 

api.add_resource(EmployeeAPI,'/')
api.add_resource(SingleEmployeeAPI,'/emp/<ID>')

if __name__=='__main__':
   app.run(host='0.0.0.0',port=5001)