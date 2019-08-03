from . import db

class  Example(db.Model):
	__tablename__ = "example"
	id = db.Column(db.Integer, primary_key=True)
	info = db.Column(db.String, )
	name = db.Column(db.String, )
	city = db.Column(db.String, )

	def __repr__(self):
		return '<Example {}>'.format(self.info)