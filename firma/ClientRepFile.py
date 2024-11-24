class ClientRepFile:

    def __init__(self, file_strategy):
        self._data = []
        self._file_strategy = file_strategy

    def write_data_to_file(self):
        self._file_strategy.write_data_to_file(self._data)

    def read_data_from_file(self):
        self._data = self._file_strategy.read_data_from_file()

    def get_short_list(self, skip=None, count=None):
        return self._data[skip:][:count]

    def get(self, id):
        index = self.__ids().index(id)
        return self._data[index]

    def delete(self, id):
        ids = self.__ids()
        self._data.remove(self._data[ids.index(id)])

    def change(
        self,
        id,
        email=None,
        phone_number=None,
        firstname=None,
        surname=None,
        fathersname=None,
        pasport=None,
        balance=None,
    ):
        ids, emails = self.__ids(), self.__emails()
        index = ids.index(id)
        data = self._data[index]
        if email != self._data[index]['email'] and email in emails:
            raise ValueError('Поле email - уникально.')
        if email:
            data['email'] = email
        if phone_number:
            data['phone_number'] = phone_number
        if firstname:
            data['firstname'] = firstname
        if surname:
            data['surname'] = surname
        if fathersname:
            data['fathersname'] = fathersname
        if pasport:
            data['pasport'] = pasport
        if balance:
            data['balance'] = balance

        self._data[index] = data

    def add(
        self, 
        email,
        phone_number,
        firstname, 
        surname, 
        fathersname,
        pasport,
        balance,
    ):
        ids, emails = self.__ids(), self.__emails()
        if email in emails:
            raise ValueError('Поле email - уникально.')
        if not email:
            raise ValueError('Поле email - не может быть пустым.')
        if not firstname:
            raise ValueError('Поле Имя - не может быть пустым.')
        if not surname:
            raise ValueError('Поле Фамилия - не может быть пустым.')
        ids.sort()

        id = 0
        if ids:
            id = ids[-1]
        id += 1

        self._data.append(
            {
                'id': id,
                'email': email,
                'phone_number': phone_number,
                'firstname': firstname, 
                'surname': surname, 
                'fathersname': fathersname,
                'pasport': pasport,
                'balance': balance,
            }
        )

    def get_count(self):
        return len(self._data)

    def __ids(self):
        return [entry['id'] for entry in self._data]

    def __emails(self):
        return [entry['email'] for entry in self._data]
