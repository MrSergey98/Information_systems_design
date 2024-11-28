from http.server import BaseHTTPRequestHandler, HTTPServer

from webapp.CreateClientWebController import CreateClientWebController
from webapp.DetailsClientWebController import DetailsClientWebController
from webapp.MainWebController import MainWebController

class PathMapperHttp(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/':
            MainWebController(self)

        if self.path == '/client_new':
            CreateClientWebController(self)

        if self.path == '/client_delete':
            DeleteClientWebController(self)

        if self.path.split('/')[1] == 'client_details':
            DetailsClientWebController(self)


    def do_POST(self):

        if self.path == '/client_new':
            CreateClientWebController(self)

        if self.path == '/client_delete':
            DeleteClientWebController(self)

        if self.path == '/client_details':
            DetailsClientWevController(self)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8080
    server = HTTPServer((HOST, PORT), PathMapperHttp)
    server.serve_forever()
    server.server_close()
