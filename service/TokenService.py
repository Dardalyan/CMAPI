import jwt
import datetime
from app_config.config import settings


class TokenService:
    __SECRET_KEY = settings.secret_key

    def generate_token(self) -> str:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            "iat": datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, self.__SECRET_KEY, algorithm=settings.encryption_alg)
        return token

    def verify_token(self, token: str):
        decoded_token = jwt.decode(token, self.__SECRET_KEY, algorithms=[settings.encryption_alg])
        return decoded_token
