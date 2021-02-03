from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('login')
def login():
	return "<h1>This is the login page</h1>"