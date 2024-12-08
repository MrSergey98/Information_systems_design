from firma.CreateClientWindow import CreateClientWindow
from root.settings import jinja_env
from webapp.BasicWebController import BasicController


class CreateClientController(BasicController):

    def get_app_view(self, **kwargs):
        self.view = None  # Инициализируем как None
        self.parent = kwargs.get('parent')
        self.show_window()

    def show_window(self):
        if self.view is None or not self.view.winfo_exists():
            self.view = CreateClientWindow(self.parent)
            self.setup_handlers()

    def setup_handlers(self):
        self.view.bind_create_button(self.create_client)
        self.view.protocol("WM_DELETE_WINDOW", self.on_closing)

    def validate_data(self, client_data):
        errors = []
        if not client_data['firstname'].strip():
            errors.append("Имя не может быть пустым")
        if not client_data['surname'].strip():
            errors.append("Фамилия не может быть пустой")
        if '@' not in client_data['email']:
            errors.append("Неверный формат email")
        return errors

    def create_client(self):
        client_data = self.view.get_form_data()
        errors = self.validate_data(client_data)

        if errors:
            self.view.show_errors(errors)
            return

        self.repository.add(
            firstname=client_data.get('firstname'),
            surname=client_data.get('surname'),
            fathersname=client_data.get('fathersname'),
            email=client_data.get('email'),
            phone_number=client_data.get('phone_number'),
            pasport=client_data.get('pasport'),
            balance=client_data.get('balance'),
        )
        self.view.notify_observers(self.repository.get_short_list())
        self.view.destroy()

    def on_closing(self):
        if self.view:
            self.view.destroy()
            self.view = None

    def get_web_view(self, **kwargs):
        context = {
            'view': 'client_new',
            'can_edit_fields': True,
            'error': kwargs.get('error'),
            'data': None,
        }
        template = jinja_env.get_template('webapp/shablon_form.html')
        return bytes(template.render(context), 'utf-8')

    def handle_post(self, data_dict):
        self.repository.add(
            email=data_dict.get('email', [None])[0],
            phone_number=data_dict.get('phone_number', [None])[0],
            firstname=data_dict.get('firstname', [None])[0],
            surname=data_dict.get('surname', [None])[0],
            fathersname=data_dict.get('fathersname', [None])[0],
            pasport=data_dict.get('pasport', [None])[0],
            balance=data_dict.get('balance', [None])[0],
        )
