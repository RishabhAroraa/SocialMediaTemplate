from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '$3cr3t-k3Y'

	from .views import views
	app.register_blueprint(views, url_prefix='/')

	return app
