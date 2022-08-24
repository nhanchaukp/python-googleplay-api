from http.server import BaseHTTPRequestHandler, HTTPServer
from google_play_scraper import app
import json, os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        spath = os.path.split(self.path)
        print(spath)
        try:
            if spath[0]=='/app':
                result = app(spath[1], lang='en', country='us')
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(json.dumps(result), 'utf8'))
                return
        except:
            self.send_error(500, "Error")