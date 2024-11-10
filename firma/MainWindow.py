from tkinter import *
from tkinter import ttk
from firma.Observe import Observer

columns = ('firstname', 'surname', 'email')


class MainWindow(Tk, Observer):
    def __init__(self, data):
        super().__init__()
        self.title("Управление клиентами")
        self.geometry("600x400")

        self.create_widgets()
        self.update(data)

    def create_widgets(self):
        # Заголовок
        Label(self, text='Клиенты:', font=('Arial', 14)).pack(pady=10)

        # Таблица
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

        # Настройка заголовков таблицы
        headers = {'firstname': 'Имя', 'surname': 'Фамилия', 'email': 'Email'}
        for col in columns:
            self.tree.heading(col, text=headers[col])
            self.tree.column(col, width=100)

        # Кнопки
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        self.button_create = ttk.Button(button_frame, text='Создать клиента')
        self.button_create.pack(side=LEFT, padx=5)

        self.button_delete = ttk.Button(button_frame, text='Удалить клиента')
        self.button_delete.pack(side=LEFT, padx=5)

        ttk.Button(button_frame, text='Просмотр деталей').pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text='Обновить данные').pack(side=LEFT, padx=5)

    def update(self, data):
        # Очищаем текущие данные
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Добавляем новые данные
        for client in data:
            self.tree.insert("", END, values=[
                client[col] for col in columns
            ])