from flask import Flask,json
from flask_mail import*

app=Flask(__name__)
with open('config.json','r')as f:
    params=json.load(f) ['param']

#setting configurations for sending mail

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']=params['gmail-user']
app.config['MAIL_PASSWORD']=params['gmail-password']
app.config['MAIL_USE_TLS']=True #transport layer security
app.config['MAIL_USE_SSL']=False #secured socket layer

mail=Mail(app)

@app.route('/')
def index():
    msg = Message("Important Mail",
    sender = app.config['MAIL_USERNAME'],
    recipients = ['saurabhdropper@gmail.com'])
    msg.body="This is to inform you that your fees is pending..!!!"
    with app.open_resource("Python-Durga-Notes.pdf","rb")as fp:
        msg.attach("Python-Durga-Notes.pdf","applications/pdf",fp.read())
    mail.send(msg)
    return "Message sent successfully"

app.run(debug=True)
