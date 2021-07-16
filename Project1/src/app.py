from flask import Flask

flask_app = Flask(__name__, static_url_path='')



#this function decleration and the accompanying "decorator" allow us to define the resource that this server
#exposes to the client. A decorator takes in a function, adds some additional functionality, and returns
#said function.
@flask_app.route('/')
def hello_world():
    return "Hello World"