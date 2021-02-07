from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '8D49F882EC744223E64E7B143C6E4'

	from .views import views
	app.register_blueprint(views, url_prefix='/')

	from .auth import auth
	app.register_blueprint(auth, url_prefix='/auth/')

	return app
