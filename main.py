from flask import Flask, render_template, request
from re import match

from encrypt import hash_password
import model.auth_db as db 

app = Flask(__name__)

@app.get('/')
def index():
	return render_template('index.html')

@app.get('/login')
def login():
	return render_template('login.html')

@app.get('/register')
def register():
	return render_template('register.html')


@app.post('/register')
def post_register():
	email = request.form['email']
	plain_text = request.form['password']
	plain_text_confirm = request.form['confirm-password']

	regx_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

	verify_email = match(regx_email, email)
	if plain_text != plain_text_confirm :
		return register();

	regx_plain_text = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
	verify_plain_text = match(regx_plain_text, plain_text)

	print(verify_email, verify_plain_text)


	# if not (verify_plain_text and verify_email):
	# 	return register(); 

	password = hash_password(plain_text)
	print(email, password)
	return 'you register successfully!'





if __name__ == '__main__':
	app.run(
		host="127.0.0.1",
		port="5000",
		debug=True
		)