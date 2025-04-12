from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.DocumentController import DocumentController
from controller.MailController import MailController
from controller.AuthController import AuthController
from middleware.AuthMiddleware import TokenMiddleware
from app_config.config import settings

app = FastAPI()

# Controllers
documentController = DocumentController()
mailController = MailController()
authController = AuthController()

# Including Controllers
app.include_router(documentController.router)
app.include_router(mailController.router)
app.include_router(authController.router)

# Middleware Settings
origins = [
    settings.cors_url_origin_1,
    settings.cors_url_origin_2
]
app.add_middleware(TokenMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
