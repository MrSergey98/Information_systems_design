import re
from datetime import date, timedelta


class ValidationError(Exception):
    pass

def validate_number(min=None, max=None, float_=False):

    def inner(value, field_name=''):
        classes_to_check = (int, )
        if float_:
            classes_to_check += (float, )
        if not isinstance(value, classes_to_check):
            raise ValidationError(f'Поле {field_name} должно быть числом')
        if min is not None and value < min:
            raise ValidationError(f'Поле {field_name} должно быть больше {min}')
        if max is not None and value > max:
            raise ValidationError(f'Поле {field_name} должно быть меньше {max}')
        return True

    return inner

def validate_id(value, field_name=''):
    validate_number(min=0)(value=value, field_name=field_name)
    return True

def validate_date(value, field_name=''):
    if not isinstance(value, (str, date)):
        raise ValueError(f'Поле {field_name} должно быть строкой или date')
    if isinstance(value, str):
        if not re.search(r'\d{2}.\d{2}.\d{4}', value):
            raise ValueError(f'Поле {field_name} должно быть в формате: <День>.<Месяц>.<Год>')

def validate_duration(value, field_name=''):
    if not isinstance(value, (str, timedelta)):
        raise ValueError(f'Поле {field_name} должно быть строкой или timedate')
    if isinstance(value, str):
        if not re.search(r'\d+:\d+', value):
            raise ValueError(f'Поле {field_name} должно быть в формате: <Дни>:<Часы>')

def validate_str(value, field_name=''):
    if not isinstance(value, str):
        raise ValidationError(f'Поле {field_name} должно быть строкой')
