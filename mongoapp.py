from flask import Flask,request,render_template,redirect,url_for
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient('mongodb://localhost:27017/')

db=client['Flask-DB']
collection=db['Users']
collection1 = db['Index']

@app.route('/add_data',methods=['POST'])
def add_data():
    data=request.json
    collection.insert_one(data)
    return 'Data Added to MongoDB'
@app.route('/')
def index():
    return render_template('indexform.html')

from  bcrypt import hashpw,gensalt

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password'] 
        form_data={
            'name':name,
            'email':email,
            'password':password
        }  
        if 'password' in form_data:
            form_data['password']=hashpw(form_data['password'].encode('utf-8'),gensalt())
        collection1.insert_one(form_data)
        return redirect(url_for('index')) 

app.run(host='0.0.0.0',port=5008)
    