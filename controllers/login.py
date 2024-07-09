from flask import render_template, request, make_response
from token import generate_token
from encrypt import verify_password
from models.login import select_table

def get_login(email_error=None,  password_error=None):
	email = request.cookies.get('email')
	password = request.cookies.get('password')

	if email :
		return "<h1>you already logged in</h1>"
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
		token = generate_token(email)
		resp = make_response('<h1>login successfully </h1>')
		resp.set_cookie('token' , token, httponly=True,secure=True,samesite='Strict', max_age=3600 )
		return resp;
	else:
		return get_login(None , "Incorrect password") 




