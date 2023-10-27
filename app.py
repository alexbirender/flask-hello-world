from flask import Flask
from dotenv import load_dotenv

load_dotenv(".secret_npm")

import os

app = Flask(__name__)

print(os.getenv('ENV'))
print(os.getenv('DB'))
print(os.getenv('DB222'))


@app.route('/')
def hello_world():
    return 'Hello, World!'

