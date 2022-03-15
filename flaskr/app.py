from flask import Flask
from flask import render_template, url_for,request
from flaskr import db ##look at this file from run.py but whyyyyyyyyyyy
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

id = 0

@app.route('/')
def index():
    db.creat_names_table()
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    name = request.form['name']
    
    con = sqlite3.connect(DATABASE)
    db_names = con.execute('SELECT * FROM names').fetchall()
    global id
    id = len(db_names)
    
    con.execute('INSERT INTO names VALUES(?, ?)', [id, name])
    con.commit()
    con.close()
    
    return render_template('confirm.html', name = name)

@app.route('/your_name', methods=['GET'])
def your_name():
    req = request.args
    name = req.get("name")
    
    con = sqlite3.connect(DATABASE)
    db_names = con.execute('SELECT * FROM names').fetchall()
    global id
    id = len(db_names)
    
    con.execute('INSERT INTO names VALUES(?, ?)', [id, name])
    con.commit()
    con.close()
    
    return render_template('confirm.html', name = name)

@app.route('/cheer', methods=['POST'])
def cheer():
    con = sqlite3.connect(DATABASE)
    db_names = con.execute('SELECT * FROM names').fetchall()
    con.close()
    
    name = db_names[id]
    
    return render_template('cheer.html', name = name[1])

if __name__ == "__main__":
    app.run(debug=True)