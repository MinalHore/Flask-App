from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name="Test User"
    return render_template('index.html',test_name=name)

@app.route('/list')
def list_data():
    list_elements =['AAAP','TESL','MSE','MICRO','TCS']
    return render_template('list.html',ticker=list_elements)
@app.route('/users')
def user_list():
    users =[
        {'names':'Prarik Sir','age':24,'Trainer':'DSA'},
        {'names':'Nikhil Sir','age':28,'Trainer':'React'},
        {'names':'Sudhir Sir','age':32,'Trainer':'java/python'},
        {'names':'Saurabh Sir','age':24,'Trainer':'full stack'},
        
    ]

    return render_template('users.html',test_users=users)

@app.route('/dict')
def user_dict():
    users={
        1:{'names':'Prarik Sir','age':24,'Trainer':'DSA'},
        2:{'names':'Nikhil Sir','age':28,'Trainer':'React'},
        3:{'names':'Sudhir Sir','age':32,'Trainer':'java/python'},
        4:{'names':'Saurabh Sir','age':24,'Trainer':'full stack'},
        
    }
    return render_template('dict.html',dict_users=users) 

if __name__=='__main__':
   app.run(host='0.0.0.0',port=5005)