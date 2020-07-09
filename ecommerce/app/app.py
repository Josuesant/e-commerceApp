from flask import Flask
from configmodule import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig())


@app.route('/')
def hello():
	return 'Hello Py!'


@app.route('/<name>')
def hello_name(name):
	return 'Hello {}!'.format(name)
