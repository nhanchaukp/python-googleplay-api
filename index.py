from flask import Flask, Response

app = Flask(__name__)
 
@app.route('/')
def home():
    return 'You are at home page.'