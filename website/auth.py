from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		data = request.form
		uname = data.get('uname')
		email = data.get('email')
		passwd = data.get('passwd')
		passwd2 = data.get('passwd2')
		print('New signup-> \nName: {}\nPassword: {}\nEmail: {}'.format(uname, passwd, email))

		if(passwd != passwd2):
			flash("Passwords do not match.", category='error')

	return render_template('signup.html')


@auth.route('login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		data = request.form
		uname = data.get('uname')
		passwd = data.get('passwd')
		print('New login-> \nName: {}\nPassword: {}\n'.format(uname,passwd))

	return render_template('login.html')


@auth.route('logout')
def logout():
	return "<h1>Logged out</h1>"