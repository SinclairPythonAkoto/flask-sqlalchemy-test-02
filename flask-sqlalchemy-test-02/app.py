import os
import psycopg2
from flask import Flask, render_template, g, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

DATABASE_URL = os.environ.get('postgres://fikwczdiymxhwf:73bf42c2c8a15fa59b77e93654b6383e1cf4f85bdf0156818d1cf39a77815f13@ec2-54-243-47-196.compute-1.amazonaws.com:5432/d3uburco4fea1b')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page_2')
def page_2():
	return render_template("random_page_2.html")

@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/view_database')
def view_db():
	conn = psycopg2.connect(DATABASE_URL)
	db = conn.cursor()
	data = db.execute("SELECT * FROM example")
	return render_template('view_database.html', data=data)

