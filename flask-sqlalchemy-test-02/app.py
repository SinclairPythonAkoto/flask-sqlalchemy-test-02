import os
import psycopg2
from flask import Flask, render_template, g, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import db, Example


#DATABASE_URL = os.environ.get('postgres://fikwczdiymxhwf:73bf42c2c8a15fa59b77e93654b6383e1cf4f85bdf0156818d1cf39a77815f13@ec2-54-243-47-196.compute-1.amazonaws.com:5432/d3uburco4fea1b')


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
	#data = Example.query.filter_by(info=info).first_or_404()

	# query = "SELECT * FROM example"
	# data = db.execute(query)
	# return render_template('view_database.html', data=data)

	conn = psycopg2.connect('')
	cur = conn.cursor()
	data = cur.execute("SELECT * FROM example")
	cur.close()
	conn.close()
	return render_template('view_database.html', data=data)

