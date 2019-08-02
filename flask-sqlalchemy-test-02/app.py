import os
import psycopg2
from flask import Flask, render_template, g, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fikwczdiymxhwf:73bf42c2c8a15fa59b77e93654b6383e1cf4f85bdf0156818d1cf39a77815f13@ec2-54-243-47-196.compute-1.amazonaws.com:5432/d3uburco4fea1b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)

# heroku = Heroku(app)
# db = SQLAlchemy(app)

class  Example(db.Model):
	__tablename__ = "example"
	id = db.Column(db.Integer, primary_key=True)
	info = db.Column(db.String, )
	name = db.Column(db.String, )
	city = db.Column(db.String, )



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
def view_db(info):
	#data = Example.query.filter_by(info=info).first_or_404()

	# query = "SELECT * FROM example"
	# data = db.execute(query)
	# return render_template('view_database.html', data=data)

	conn = psycopg2.connect(DATABASE_URL)
	cur = conn.cursor()
	data = cur.execute("SELECT * FROM example")
	cur.close()
	conn.close()
	return render_template('view_database.html', data=data)

