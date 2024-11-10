
from firma.ClientRepFileAdapter import ClientRepFileAdapter
from firma.ClientRepFile import ClientRepFile
from firma.ClientRepJson import ClientRepJson
from firma.MainWindow import MainWindow
from firma.CreateClientController import CreateClientController


class MainWindowController:
    def __init__(self):
        self.repository = ClientRepFileAdapter(ClientRepFile(ClientRepJson))
        self.main_window = MainWindow(data=self.repository.get_short_list())
        self.create_controller = None  # Добавляем атрибут для хранения контроллера
        self.setup_handlers()
        self.main_window.mainloop()

    def setup_handlers(self):
        self.main_window.button_create.configure(command=self.open_create_window)

    def open_create_window(self):
        # Создаём новый контроллер только если предыдущий не существует
        # или его окно было закрыто
        if (self.create_controller is None or
                not hasattr(self.create_controller, 'view') or
                not self.create_controller.view or
                not self.create_controller.view.winfo_exists()):
            self.create_controller = CreateClientController(self.main_window, self.repository)


if __name__ == "__main__":
    MainWindowController()