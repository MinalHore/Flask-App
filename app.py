from flask import Flask,jsonify,request,render_template

app=Flask(__name__)


@app.route('/app')
def home():
    return '<h1>Hello,Flask App!</h1><p>This is my testing app</p><p>This is my home page</p>'

@app.route('/<name>/<int:age>')
def test(name,age):
    return f"Hello my name is,{name},and my age is {age}"


@app.route('/handle',methods=['GET'])
def handle_args_kwargs(*args,**kwargs):

    args=request.args.getlist('args')
    kwargs={key:value for key,value in request.args.items() if key !='args'}

    args_list = list(args)
    kwargs_dict=dict(kwargs)

    result = {
        'args':args_list,   #multiple agruments
        'kwargs':kwargs_dict  #key value pairs
    }

    return jsonify(result)

@app.route('/web')
def webpage():
    return render_template('home.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')


app.run(debug=True)


#http://127.0.0.1:5000/handle?args=apple&args=banana&color=red&size=large

if __name__== "__main__":
    app.run(host='0.0.0.0',port=5001)