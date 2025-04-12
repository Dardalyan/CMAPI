from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from service.AuthService import AAuthService
from service.TokenService import TokenService

from app_config.config import settings


class AuthController:

    def __init__(self):
        self.authService = AAuthService()
        self.tokenService = TokenService()
        self.router = APIRouter()
        self.router.add_api_route(settings.login_url, self.login, methods=["POST"])

    async def login(self, request: Request):

        """
        Authenticates a user based on the provided username and password.

        The JSON body of the request must contain the following fields:
            - 'username': The username of the user attempting to log in.
            - 'password': The password associated with the username.
        """


        try:
            body = await request.json()
            username = body.get("username")
            password = body.get("password")

            is_authenticated = self.authService.authenticate(username, password)

            if is_authenticated:
                token = self.tokenService.generate_token()
                return JSONResponse(status_code=200, content={"message": "Login successful !", "token": token})

            else:
                return JSONResponse(status_code=401, content={"alert": "Invalid credentials !"})

        except Exception as e:
            print(e)
            return JSONResponse(status_code=400, content={"alert": "Authentication failed !"})
