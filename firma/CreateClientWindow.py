# CreateClientWindow.py
import tkinter as tk
from tkinter import ttk, messagebox
from firma.Observe import Observable


class CreateClientWindow(Observable, tk.Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.title("Создание клиента")
        self.geometry("400x300")
        self.resizable(False, False)  # Запрещаем изменение размера окна

        self.create_widgets()
        self.register_observer(parent)

    def create_widgets(self):
        labels = ['Имя:', 'Фамилия:', 'Отчество:', 'Email:', 'Номер телефона:', 'Паспорт:', 'Баланс:']
        self.entries = {}

        for i, label_text in enumerate(labels):
            tk.Label(self, text=label_text).grid(row=i, column=0, padx=5, pady=5)
            self.entries[label_text] = tk.Entry(self)
            self.entries[label_text].grid(row=i, column=1, padx=5, pady=5)

        self.create_button = ttk.Button(self, text='Создать')
        self.create_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

    def bind_create_button(self, callback):
        self.create_button.config(command=callback)

    def get_form_data(self):
        return {
            'firstname': self.entries['Имя:'].get(),
            'surname': self.entries['Фамилия:'].get(),
            'email': self.entries['Email:'].get(),
            'fathersname': self.entries['Отчество:'].get(),
            'pasport': self.entries['Паспорт:'].get(),
            'balance': self.entries['Баланс:'].get(),
            'phone_number': self.entries['Номер телефона:'].get(),
        }

    def show_errors(self, errors):
        messagebox.showerror("Ошибка", "\n".join(errors))