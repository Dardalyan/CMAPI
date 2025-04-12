import bcrypt

from model.User import Admin


class AuthService:

    def authenticate(self, username, password):
        pass


# Admin Auth Service
class AAuthService(AuthService):

    def __init__(self):
        self.__admin = Admin()

    def authenticate(self, username: str, password: str):
        """
        Authenticates the admin user by verifying the provided username and password.

        :param username: The username provided for authentication.
        :type username: str

        :param password: The password provided for authentication.
        :type password: str

        :return: `True` if the username and password match the admin credentials, otherwise `False`.
        :rtype: bool
        """


        if username == self.__admin.get_username():
            return self.__check_password(password)
        else:
            return False

    def __check_password(self, password: str) -> bool:
        """
        Verifies the provided password against the stored admin password using bcrypt.

        :param password: The password to verify.
        :type password: str

        :return: `True` if the password matches the stored password, otherwise `False`.
        :rtype: bool
        """
        return bcrypt.checkpw(password.encode(), self.__admin.get_password().encode())
