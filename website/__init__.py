from flask import Flask
from flaks_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)
	app.config['SECRET_KEY'] = '8D49F882EC744223E64E7B143C6E4'

	from .views import views
	app.register_blueprint(views, url_prefix='/')

	from .auth import auth
	app.register_blueprint(auth, url_prefix='/auth/')

	import .models as models

	return app

def create_database(app):
	if not path.exists('website/ ' + DB_NAME):
		db.create_all(app=app)
		print("Created Database.")
	return app
