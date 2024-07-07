from flask import Flask, render_template, request

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
	password = request.form['password']

	print(email, password)
	return 'you register successfully!'





if __name__ == '__main__':
	app.run()