from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)


@app.route('/',methods=['GET'])
def test_form():
    return render_template('testform.html')

form_data=[]

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        form_data.append({'name':name,'age':age,'city':city})
        return redirect(url_for('display_data'))

@app.route('/data')
def display_data():
    return render_template('data.html',test_data=form_data)

if __name__=='__main__':
   app.run(host='0.0.0.0',port=5001)
