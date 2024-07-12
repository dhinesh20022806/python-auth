from flask import Flask


from routers.home import home_blueprint
from routers.login import login_blueprint
from routers.register import register_blueprint



app = Flask(__name__)

app.register_blueprint(home_blueprint, url_prefix='/')

app.register_blueprint(login_blueprint,url_prefix='/login')

app.register_blueprint(register_blueprint, url_prefix='/register')


if __name__ == '__main__':
	app.run(
		host="127.0.0.1",
		port="5000",
		debug=True
		)