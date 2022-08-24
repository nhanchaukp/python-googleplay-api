from flask import Flask, Response
from google_play_scraper import app
import json

app = Flask(__name__)
 
@app.route('/')
def home():
    return 'You are at home page.'

@app.route('/apps/<path:appid>')
def apps(appid):
    result = app(appid)
    return json.dumps(result)