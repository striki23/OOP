import abc
import string


class BaseUser(abc.ABC):
    """Абстрактный класс пользователя."""

    @abc.abstractmethod
    def get_fullname(self):
        pass

    @abc.abstractmethod
    def get_username(self):
        pass


class User(BaseUser):

    def get_fullname(self):
        print()

    def get_username(self):
        print('login')


class Language(abc.ABC):

    @abc.abstractmethod
    def get_alphabet(self):
        pass


class EngAlphabet(Language):
    def get_alphabet(self):
        return string.ascii_lowercase


if __name__ == '__main__':
    user_1 = User()
