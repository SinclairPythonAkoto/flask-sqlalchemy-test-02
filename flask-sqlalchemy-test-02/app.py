import os
import psycopg2
from flask import Flask, render_template, g, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fikwczdiymxhwf:73bf42c2c8a15fa59b77e93654b6383e1cf4f85bdf0156818d1cf39a77815f13@ec2-54-243-47-196.compute-1.amazonaws.com:5432/d3uburco4fea1b'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy() # creating database object
# db.init_app(app) # pass app to the database

# Session = sessionmaker(bind = db)
# session = Session()


# heroku = Heroku(app)
# db = SQLAlchemy(app)
from sqlalchemy.orm import sessionmaker


from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine(os.getenv("DATABASE_URL"), echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()






class  Example(Base):
	__tablename__ = "example"
	id = Column(Integer, primary_key=True)
	info = Column(String, )
	name = Column(String, )
	city = Column(String, )

	# def __repr__(self):
	# 	return '<Example {}>'.format(self.info)



#DATABASE_URL = os.environ.get('DATABASE_URL', '')
#DATABASE_URL = 'postgres://fikwczdiymxhwf:73bf42c2c8a15fa59b77e93654b6383e1cf4f85bdf0156818d1cf39a77815f13@ec2-54-243-47-196.compute-1.amazonaws.com:5432/d3uburco4fea1b'


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
	
	Session = sessionmaker(bind = engine)
	session = Session()
	data = session.query(Example).all()


	#data = db.select([example])
	#data = db.execute("SELECT * FROM example").fetchall()
	#print(data)

	# db.close()
	# conn.close()
	return render_template('view_database.html', data=data)

