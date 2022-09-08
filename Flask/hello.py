from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

''' 
This simple Flask app was gotten from https://phoenixnap.com/kb/install-flask to test Flask after installation
'''