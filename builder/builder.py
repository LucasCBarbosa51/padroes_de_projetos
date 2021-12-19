from abc import ABC, abstractmethod
from typing import List


class User:
    """
    A classe user representa o Produto
    args:
        first_name (str): primeiro nome do usuário
        last_name (str): último nome do usuário
        age (int): Idade do usuário
        phone_numbers (List[str]): lista com números de telefone do usuário ('(99)9 8888-8888')
        addresses (List[str]): lista com endereços
    """
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone_numbers: List[str] = []
        self.addresses: List[str] = []

    def __repr__(self):
        """Sobrecarga em __repr__ para exibir os atributos da classe User"""
        return f'User(first_name={self.first_name}, last_name={self.last_name}, age={self.age}, ' \
               f'phone_numbers={self.phone_numbers}, addresses={self.addresses})'


class UserBuilder(ABC):
    """Builder para user"""
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
        """Adiciona um firt name para o 'produto' user"""
        self._result.first_name = first_name

    def add_last_name(self, last_name):
        """Adiciona um last name para o 'produto' user"""
        self._result.last_name = last_name

    def add_age(self, age):
        """Adiciona um age para o 'produto' user"""
        self._result.age = age

    def add_phone(self, phone):
        """Adiciona um número de telefone para o 'produto' user"""
        self._result.phone_numbers.append(phone)

    def add_address(self, address):
        """Adiciona um endereço para o 'produto' user"""
        self._result.addresses.append(address)


class UserDirector:

    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, first_name, last_name, age):
        """
        Cria um User com primeiro nome, último nome e idade
        args:
            first_name (str): primeiro nome do usuário
            last_name (str): último nome do usuário
            age (int): Idade do usuário
        """
        self._builder.add_first_name(first_name=first_name)
        self._builder.add_last_name(last_name=last_name)
        self._builder.add_age(age=age)
        return self._builder.result

    def with_age_and_address(self, first_name, last_name, age, address):
        """
        Cria um User com primeiro nome, último nome e idade
        args:
            first_name (str): primeiro nome do usuário
            last_name (str): último nome do usuário
            age (int): Idade do usuário
            address (str): endereço do usuário
        """
        self._builder.add_first_name(first_name=first_name)
        self._builder.add_last_name(last_name=last_name)
        self._builder.add_age(age=age)
        self._builder.add_address(address=address)
        return self._builder.result
