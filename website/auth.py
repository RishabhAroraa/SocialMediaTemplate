from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('signup', methods=['GET', 'POST'])
def signup():
	data = request.form
	print(data)
	return render_template('signup.html')

@auth.route('login', methods=['GET', 'POST'])
def login():
	data = request.form
	print(data)
	return render_template('login.html')

@auth.route('logout')
def logout():
	return "<h1>Logged out</h1>"
