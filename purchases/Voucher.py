from datetime import date, timedelta

from common_utils.validators import validate_number, validate_str, validate_date, validate_duration


class Voucher:

    validators = {
        'validate_price': [validate_number(min=0, float_=True)],
        'validate_place': [validate_str],
        'validate_date': [validate_date],
        'validate_duration': [validate_duration],
    }

    def __init__(self, **kwargs):
        self.price = kwargs.get('price')
        self.place = kwargs.get('place')
        self.date = kwargs.get('date')
        self.duration = kwargs.get('duration')


    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        validators = self.validators.get(f'validate_{key}')
        for validator in validators:
            validator(value, field_name=key)
        if key == 'date':
            if isinstance(value, str):
                day, month, year = map(int, value.split('.'))
                super().__setattr__(key, date(year=year, month=month, day=day))
                return
        if key == 'duration':
            if isinstance(value, str):
                days, hours = map(int, value.split(':'))
                super().__setattr__(key, timedelta(days=days, hours=hours))
                return
        super().__setattr__(key, value)

    def __str__(self):
        return f'Путевка в {self._place} на {self._date}'

    def __hash__(self):
        return hash(self._date) + hash(self._place) + hash(self._duration)