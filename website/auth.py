from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('login')
def login():
	return "<h1>Logged in</h1>"

@auth.route('logout')
def logout():
	return "<h1>Logged out</h1>"