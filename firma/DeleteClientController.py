from firma.DeleteClientWindow import DeleteClientWindow


class DeleteClientController:

    def __init__(self, parent, repository):
        self.repository = repository
        self.view = None
        self.parent = parent
        self.show_window()

    def show_window(self):
        if self.view is None or not self.view.winfo_exists():
            self.view = DeleteClientWindow(self.parent)
            self.setup_handlers()

    def setup_handlers(self):
        self.view.bind_confirm_button(self.delete_client)
        self.view.bind_close_button(self.on_closing)
        self.view.protocol("WM_DELETE_WINDOW", self.on_closing)

    def delete_client(self):
        data = self.parent.tree.selection()
        errors = self.validate_data(data)
        if errors:
            self.view.show_errors(errors)
            self.on_closing()
            return
        tree_index = int(data[0][1:])-1
        client_for_deletion_id = self.repository.get_short_list()[tree_index].get('id')
        self.repository.delete(client_for_deletion_id)
        self.view.notify_observers(self.repository.get_short_list())
        self.view.destroy()

    def validate_data(self, data):
        errors = []
        if len(data)>1:
            errors.append("Выбрано больше 1 клиента")
        if not data:
            errors.append("Не выбран клиент для удаления")
        return errors

    def on_closing(self):
        if self.view:
            self.view.destroy()
            self.view = None
