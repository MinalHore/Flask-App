from flask import Flask,request,render_template,flash,redirect,url_for

app = Flask(__name__)
app.secret_key='supersecretkey'

@app.route('/form',methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username=='Minal' and password =='1234':
        return f'you have logged in successfully,{username}'
    else:
        return 'Invalid Credentials,please try again'

@app.route('/home')
def home():
    return 'Welcome to my page!!!'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        if not username or not password:
            flash('Both fields are required','error')
            return redirect(url_for('register'))
        else:
            flash('Registration successfully') 
            return redirect(url_for('home'))
    return render_template('register.html')

app.run(debug=True)

