from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
	#TODO : check for set cookies
	return render_template('home.html')