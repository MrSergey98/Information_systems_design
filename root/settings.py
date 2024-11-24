from pathlib import Path
import jinja.src.jinja2 as jinja2

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
jinja_env.globals['fields'] = {
    'email' : 'Email',
    'firstname': 'Имя',
    'surname': 'Фамилия',
    'fathersname': 'Отчество',
    'phone_number': 'Номер телефона',
    'pasport': 'Паспорт',
    'balance': 'Баланс',
}