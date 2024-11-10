# CreateClientController.py
from firma.CreateClientWindow import CreateClientWindow

class CreateClientController:
    def __init__(self, parent, repository):
        self.repository = repository
        self.view = None  # Инициализируем как None
        self.parent = parent
        self.show_window()  # Вызываем метод для создания окна

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