from root.settings import jinja_env
from webapp.BasicWebController import BasicWebController


class DetailsClientWebController(BasicWebController):

    def handle_post(self):
        pass

    def handle_get(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        client_id = int(self.request_handler.path.split('/')[-1])
        context = {
            'view': 'client_new',
            'can_edit_fields': False,
            'data': self.repository.get(id=client_id),
            'error': None,
        }
        template = jinja_env.get_template('webapp/shablon_form.html')
        self.request_handler.wfile.write(bytes(template.render(context), 'utf-8'))
