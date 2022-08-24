from http.server import BaseHTTPRequestHandler, HTTPServer
from google_play_scraper import app
from cowpy import cow
import json

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
                message = cow.Cowacter().milk(json.dumps(result))
                self.wfile.write(message.encode())
                return
            else:
                return super(handler, self).send_head()
        except:
            self.send_error(500, "Error")