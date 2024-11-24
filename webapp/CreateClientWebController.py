from sre_constants import error

from root.settings import jinja_env
from webapp.BasicWebController import BasicWebController
from urllib.parse import parse_qs

class CreateClientWebController(BasicWebController):

    def handle_get(self, error=None):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        context = {
            'view': 'client_new',
            'can_edit_fields': True,
            'error': error,
        }
        template = jinja_env.get_template('webapp/shablon_form.html')
        self.request_handler.wfile.write(bytes(template.render(context), 'utf-8'))

    def handle_post(self):
        binary_data = self.request_handler.rfile.read(int(self.request_handler.headers['Content-Length']))
        data_dict = parse_qs(binary_data.decode())
        try:
            self.repository.add(
                email=data_dict.get('email', [None])[0],
                phone_number=data_dict.get('phone_number', [None])[0],
                firstname=data_dict.get('firstname', [None])[0],
                surname=data_dict.get('surname', [None])[0],
                fathersname=data_dict.get('fathersname', [None])[0],
                pasport=data_dict.get('pasport', [None])[0],
                balance=data_dict.get('balance', [None])[0],
            )
        except ValueError as e:
            self.handle_get(error=e)
        else:
            self.request_handler.send_response(301)
            self.request_handler.send_header('Location', '/')
            self.request_handler.end_headers()
