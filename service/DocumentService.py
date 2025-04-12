from model.Document import Document
from app_config.config import settings
from app_config.firebase_config import db


class DocumentService:

    def __init__(self):
        self.__filePath = settings.storage_path
        self.cl = db.collection(settings.collection_name)

    def getAllDocuments(self) -> list:
        result = self.cl.get()
        docs = [doc.to_dict() for doc in result if doc.exists and doc.id != 'TEST']
        return docs

    def getDocumentByDocCode(self, dc: str) -> dict | None:
        doc = self.cl.document(dc).get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def addDocument(self, doc: Document):
        self.cl.document(doc.getDocCode()).set(doc.getDict())

    def removeDocument(self, dc: str):
        self.cl.document(dc).delete()
