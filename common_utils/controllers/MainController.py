from common_utils.controllers.CreateClientController import CreateClientController
from common_utils.controllers.DeleteClientController import DeleteClientController
from firma.MainWindow import MainWindow
from root.settings import jinja_env
from webapp.BasicWebController import BasicController


class MainController(BasicController):

    def get_app_view(self):
        self.main_window = MainWindow(data=self.repository.get_short_list())
        self.create_controller = None  # Добавляем атрибут для хранения контроллера
        self.delete_controller = None
        self.setup_handlers()
        self.main_window.mainloop()

    def setup_handlers(self):
        self.main_window.button_create.configure(command=self.open_create_window)
        self.main_window.button_delete.configure(command=self.open_delete_window)


    def open_create_window(self):
        # Создаём новый контроллер только если предыдущий не существует
        # или его окно было закрыто
        if (self.create_controller is None or
                not hasattr(self.create_controller, 'view') or
                not self.create_controller.view or
                not self.create_controller.view.winfo_exists()):
            self.create_controller = CreateClientController()
            self.create_controller.get_app_view(parent=self.main_window)

    def open_delete_window(self):
        if (self.delete_controller is None or
                not hasattr(self.delete_controller, 'view') or
                not self.delete_controller.view or
                not self.delete_controller.view.winfo_exists()):
            self.delete_controller = DeleteClientController()
            self.delete_controller.get_app_view(parent=self.main_window)



    def get_web_view(self, **kwargs):
        context = {
            'header': 'Hi there!',
            'data': self.repository.get_short_list()
        }
        template = jinja_env.get_template('webapp/index.html')
        return bytes(template.render(context), 'utf-8')


if __name__ == "__main__":
    MainController().get_app_view()