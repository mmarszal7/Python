from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = open('.\index.html', 'rb')
        self.wfile.write(response.read())

    def do_POST(self):
        request = self.rfile.read(int(self.headers['Content-Length'])).decode()
        self.send_response(200)
        self.end_headers()
		
        print(request)
        file = open('resulst.txt', 'a')
        file.write(request + '\n')
        file.close()
		

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()