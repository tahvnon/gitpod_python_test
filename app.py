from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(f'request incoming {request}')
    return 'Hello, World!'

