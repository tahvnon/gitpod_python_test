from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('request incoming')
    return 'Hello, World!'