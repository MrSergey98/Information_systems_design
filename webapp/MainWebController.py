from webapp.BasicWebController import BasicWebController
from root.settings import jinja_env


class MainWebController(BasicWebController):

    def handle_get(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        context = {
            'header': 'Hi there!',
            'data': self.repository.get_short_list()
        }
        template = jinja_env.get_template('webapp/index.html')
        self.request_handler.wfile.write(bytes(template.render(context), 'utf-8'))

    def handle_post(self):
        pass
