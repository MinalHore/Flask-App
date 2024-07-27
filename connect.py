from  flask import Flask,render_template
import sqlite3

conn = sqlite3.connect('sqlite-sakila.db')
conn.row_factory = sqlite3.Row
print("Open the database successfully")

cur=conn.cursor()

app=Flask(__name__)


@app.route('/sql')
def sql_data():
    conn=sqlite3.connect('sqlite-sakila.db')
    conn.row_factory=sqlite3.Row
    print("============Opened the database successfully in our python function=======")
    cur=conn.cursor()
    sql="""SELECT *from customer"""
    print(sql)
    
    cur.execute(sql)
    results=cur.fetchall()
    return render_template('test.html',test=results)
    
if __name__=='__main__':
   app.run(host='0.0.0.0',port=5007)