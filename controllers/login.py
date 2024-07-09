from flask import render_template, request

from encrypt import verify_password
from models.login import select_table

def get_login(email_error=None,  password_error=None):
	return render_template('login.html', email_error=email_error, password_error=password_error )

def post_login():
	email = request.form['email']
	password = request.form['password']

	print(email, password)

	data = select_table(email)

	if not data:
		return get_login("eamil doesn't exist")

	stored_email = data[0]
	stored_password = data[1]

	is_correct_password = verify_password(password , stored_password)

	if is_correct_password:
		return '<h1>login successfully </h1>'
	else:
		return get_login(None , "Incorrect password") 




