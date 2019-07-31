import os
import psycopg2
from flask import Flask, render_template, g, url_for, redirect


app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fikwczdiymxhwf:73bf42c2c8a15fa59b77e93654b6383e1cf4f85bdf0156818d1cf39a77815f13@ec2-54-243-47-196.compute-1.amazonaws.com:5432/d3uburco4fea1b'
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
	try:
	    connection = psycopg2.connect(user = "fikwczdiymxhwf",
	                                  password = "73bf42c2c8a15fa59b77e93654b6383e1cf4f85bdf0156818d1cf39a77815f13",
	                                  host = "ec2-54-243-47-196.compute-1.amazonaws.com",
	                                  port = "5432",
	                                  database = "d3uburco4fea1b")
    	db = connection.cursor()
		data = db.execute("SELECT * FROM example").fetachall()
		return render_template('view_database.html', data=data)

    except (Exception, psycopg2.Error) as error :
	    return "Error while connecting to PostgreSQL", error

    finally:
    #closing database connection.
        if(connection):
            db.close()
            connection.close()
            return redirect(url_for('view_db'))

