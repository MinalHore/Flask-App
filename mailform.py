from flask import Flask,json,render_template,request
from flask_mail import*

app=Flask(__name__)

with open('config.json','r') as f:
    params=json.load(f)['param']

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']=params['gmail-user']
app.config['MAIL_PASSWORD']=params['gmail-password']
app.config['MAIL_USE_TLS']=True #transport layer security
app.config['MAIL_USE_SSL']=False #secured socket layer

mail=Mail(app)

@app.route('/')
def mail_function():
    return render_template('mailform.html')

@app.route('/send_email',methods=['POST'])
def send_mail():
    recipient=request.form['recipient']
    subject=request.form['subject']
    body=request.form['body']
    msg=Message(subject,sender=app.config['MAIL_USERNAME'],recipients=[recipient])
    msg.body=body
    mail.send(msg)
    return 'Message send successfully'

app.run(debug=True) 

# def format_number(number):
#     if not isintance(number,(int,float))or number<0:
#         raiseValueError("The input must be a non-negative number.")
#         return f"{number:.}"
