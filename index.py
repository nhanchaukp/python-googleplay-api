from flask import Flask, Response
import google_play_scraper
import json

app = Flask(__name__)
 
@app.route('/')
def home():
    return 'You are at home page.'

@app.route('/apps/<path:appid>')
def apps(appid):
    result = google_play_scraper.app(appid)
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response