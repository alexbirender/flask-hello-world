from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

import os
print(os.getenv('ENV'))
print(os.getenv('DB'))
print(os.getenv('DB222'))
