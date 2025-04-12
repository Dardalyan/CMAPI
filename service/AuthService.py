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
        if username == self.__admin.get_username():
            return self.__check_password(password)
        else:
            return False

    def __check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.__admin.get_password().encode())
