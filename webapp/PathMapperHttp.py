from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

from common_utils.controllers.MainController import MainController
from common_utils.controllers.CreateClientController import CreateClientController
from common_utils.controllers.DeleteClientController import DeleteClientController
from common_utils.controllers.DetailsClientController import DetailsClientController


class PathMapperHttp(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = None

    def do_GET(self):

        if self.path == '/':
            self.controller = MainController()
            self.display_view()

        if self.path == '/client_new':
            self.controller = CreateClientController()
            self.display_view()

        if self.path.split('/')[1] == 'client_details':
            self.controller = DetailsClientController()
            self.display_view(client_id=int(self.path.split('/')[-1]))


    def do_POST(self):

        if self.path == '/client_new':
            data_dict = parse_qs(self.rfile.read(int(self.headers['Content-Length'])).decode())
            self.controller = CreateClientController()
            try:
                self.controller.handle_post(data_dict)
            except ValueError as e:
                self.display_view(error=e)
            else:
                self.send_300_redirect_main_headers()


        if self.path.split('/')[1] == 'client_delete':
            client_id = int(self.path.split('/')[-1])
            self.controller=DeleteClientController()
            try:
                self.controller.handle_post(client_id=client_id)
            except ValueError:
                pass
            else:
                self.send_300_redirect_main_headers()


    def send_200_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def send_300_redirect_main_headers(self):
        self.send_response(301)
        self.send_header('Location', '/')
        self.end_headers()

    def display_view(self, **kwargs):
        view = self.controller.get_web_view(**kwargs)
        self.send_200_headers()
        self.wfile.write(view)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8080
    server = HTTPServer((HOST, PORT), PathMapperHttp)
    print(f'Starting server at: http://{HOST}:{PORT}')
    server.serve_forever()
    server.server_close()
