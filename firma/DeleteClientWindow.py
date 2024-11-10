import tkinter as tk
from tkinter import ttk, messagebox

from firma.Observe import Observable


class DeleteClientWindow(Observable, tk.Toplevel):

    def __init__(self, parent):
        super().__init__()

        self.title("Удаление клиента")
        self.geometry('200x200')
        self.resizable(False, False)

        self.create_widgets()
        self.register_observer(parent)

    def create_widgets(self):
        self.label = tk.Label(self, text='Вы уверены?')
        self.label.pack()
        self.confirm_button = ttk.Button(self, text='Да')
        self.close_button = ttk.Button(self, text='Нет')
        self.confirm_button.pack()
        self.close_button.pack()

    def bind_confirm_button(self, callback):
        self.confirm_button.config(command=callback)

    def bind_close_button(self, callback):
        self.close_button.config(command=callback)

    def show_errors(self, errors):
        messagebox.showerror("Ошибка", "\n".join(errors))