from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Post(db.model):
	sno = db.Column(db.Integer, primary_key=True)
	uname = db.Column(db.String(150), db.ForeignKey('user.uname'))
	data = db.column(db.String(500))
	timestamp = db.Column(db.DateTime(timezone=True), default=func.now())

class User(db.model, UserMixin):
	uname = db.Column(db.String(150), primary_key=True)
	##fix?## 
	email = db.Column(db.String(150), unique=True)
	#######
	password = db.Column(db.String(32))
	posts = db.relationship('Post')