from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '$3cr3t-k3Y'

	from .views import views
	app.register_blueprint(views, url_prefix='/')

	from .auth import auth
	app.register_blueprint(auth, url_prefix='/')

	return app