import bcrypt
from app_config.config import settings


class User:

    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = self.__encryptPassword(password)

    def __encryptPassword(self, password: str) -> str:
        """
        Encrypts the given password.
        :param password: password of the user.
        :return:  encrypted password
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password


class Admin(User):

    def __init__(self):
        super().__init__(settings.username, settings.password)
