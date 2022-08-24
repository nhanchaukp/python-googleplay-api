from flask import Flask
from google_play_scraper import app
import json

app = Flask(__name__)
 
@app.route('/')
def home():
    return 'You are at home page.'
    
@app.route('/apps/<appid>')
def apps(appid):
    result = app(appid, lang='en', country='us')
    return json.dumps(result)
    
if __name__ == '__main__':
    app.run()