from abc import ABC, abstractmethod


class User:

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class UserBuilder(ABC):

    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def add_first_name(self, first_name):
        pass

    @abstractmethod
    def add_last_name(self, last_name):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_phone(self, phone):
        pass

    @abstractmethod
    def add_address(self, address):
        pass


class ConcreteUserBuilder(UserBuilder):
    """
    ConcreteUserBuilder cria usuários de acordo com a necessidade do cliente
    """

    def __init__(self):
        self.reset()

    def reset(self):
        """Método para resetar e criar um novo usuário do zero"""
        self._result = User()

    @property
    def result(self):
        """Cria um novo usuário"""
        user = self._result
        self.reset()
        return user

    def add_first_name(self, first_name):
        self._result.first_name = first_name

    def add_last_name(self, last_name):
        self._result.last_name = last_name

    def add_age(self, age):
        self._result.age = age

    def add_phone(self, phone):
        self._result.phone_numbers.append(phone)

    def add_address(self, address):
        self._result.addresses.append(address)


class UserDirector:

    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, first_name, last_name, age):
        self._builder.add_first_name(first_name=first_name)
        self._builder.add_last_name(last_name=last_name)
        self._builder.add_age(age=age)
        return self._builder.result
