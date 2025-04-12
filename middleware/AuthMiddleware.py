from fastapi import FastAPI
import jwt
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from service.TokenService import TokenService

from app_config.config import settings


# Token Middleware
class TokenMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):

        if request.url.path in [settings.get_all_docs_url, settings.delete_doc_url, settings.add_doc_url]:
            service = TokenService()
            auth_header = request.headers.get("Authorization")

            if not auth_header:
                return JSONResponse(status_code=401, content="Authorization header is missing !")

            try:
                token = auth_header.split("Bearer ")[1]
                service.verify_token(token)

            except jwt.ExpiredSignatureError:
                return JSONResponse(status_code=401, content="Token is expired !")

            except jwt.InvalidTokenError:
                return JSONResponse(status_code=401, content="Token is invalid !")

        response = await call_next(request)
        return response
