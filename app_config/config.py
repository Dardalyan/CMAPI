from dotenv import load_dotenv
import os
import json


load_dotenv()

class Settings:
    def __init__(self):
        self.login_url = os.getenv("URL_LOGIN")
        self.get_all_docs_url = os.getenv("URL_GET_ALL_DOCS")
        self.get_doc_url = os.getenv("URL_GET_DOC")
        self.add_doc_url = os.getenv("URL_ADD_DOC")
        self.delete_doc_url = os.getenv("URL_DELETE_DOC")
        self.mail_url = os.getenv("URL_MAIL")

        self.firebase_sdk:dict = json.loads(os.getenv("FIREBASE_SDK"))
        self.firebase_sdk["private_key"] = self.firebase_sdk["private_key"].replace("\\n", "\n")

        self.collection_name = os.getenv("COLLECTION")

        self.username: str = os.getenv("USERNAME")
        self.password: str = os.getenv("PASSWORD")

        self.storage_path = os.getenv("STORAGE_PATH")

        self.secret_key = os.getenv("SECRET_KEY")
        self.encryption_alg = os.getenv("ENCRYPTION_ALG")

        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT"))
        self.mail_sender_username = os.getenv("MAIL_SENDER_USERNAME")
        self.mail_sender_password = os.getenv("MAIL_SENDER_PASS")
        self.mail_target = os.getenv("MAIL_TARGET")

        self.cors_url_origin_1 = os.getenv("CORS_ORIGIN_URL_1")
        self.cors_url_origin_2 = os.getenv("CORS_ORIGIN_URL_2")

settings = Settings()
