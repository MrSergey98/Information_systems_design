from webapp.BasicWebController import BasicWebController


class DeleteClientWebController(BasicWebController):

    def handle_get(self):
        pass

    def handle_post(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        client_id = int(self.request_handler.path.split('/')[-1])
        self.repository.delete(id=client_id)
