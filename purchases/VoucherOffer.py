from common_utils.validators import validate_number, validate_id, ValidationError


class VoucherOffer:

    statuses = (
        'display',
        'disabled',
        'payed',
    )

    validators = {
        'validate_client_id': [validate_id],
        'validate_voucher_id': [validate_id],
        'validate_price': [validate_number(min=0, float_=True)],
        'validate_discount': [validate_number(min=0, max=100)],
    }

    def __init__(self, **kwargs):
        self.client_id = kwargs.get('client_id')
        self.voucher_id = kwargs.get('voucher_id')
        self.price = kwargs.get('price')
        self.discount = kwargs.get('discount')
        self.status = kwargs.get('status')

    def __setattr__(self, key, value):
        if key == 'status':
            self.__validate_status(value)
            super().__setattr__('status', value)
            return
        validators = self.validators.get(f'validate_{key}')
        for validator in validators:
            validator(value, field_name=key)

        super().__setattr__(key, value)

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __str__(self):
        return f'Предложение по покупке путевки #{self._voucher_id}, статус: {self._status}'

    def __validate_status(self, status):
        if not status in VoucherOffer.statuses:
            raise ValidationError(f'Неверный статус, выбор из: {self.statuses}')
