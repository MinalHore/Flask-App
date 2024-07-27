from  flask import Flask,render_template,request
from pymongo import MongoClient
from bcrypt import hashpw,gensalt

app=Flask(__name__)

mongo_uri = "mongodb+srv://minalhore34:vyNMD5b4tyQntAKd@flaskcluster.27n5sf7.mongodb.net/?retryWrites=true&w=majority&appName=FlaskCluster"
client=MongoClient(mongo_uri)

db=client['Flask-DB']
collection=db['Users']
collection1=db['Register_table']

@app.route('/add',methods=['POST'])
def add_data():
    data=request.json
    collection.insert_one(data)
    return 'Data has been added successfully'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password'].encode('utf-8')
        hashed_password=hashpw(password,gensalt())
        collection1.insert_one(
            {
                "email":email,
                "password":hashed_password
            }
        )
        return 'User has been registered successfully'
    return render_template('user_registration.html')

app.run(debug=True)