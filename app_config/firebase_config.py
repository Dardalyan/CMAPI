import firebase_admin
from firebase_admin import credentials, firestore
from .config import settings


class FirebaseSettings:

    def __init__(self):
        self.cred = credentials.Certificate(settings.firebase_sdk)
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()


db = FirebaseSettings().db
