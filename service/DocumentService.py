from model.Document import Document
from app_config.config import settings
from app_config.firebase_config import db


class DocumentService:

    def __init__(self):
        self.__filePath = settings.storage_path
        self.cl = db.collection(settings.collection_name)

    def getAllDocuments(self) -> list:
        """
        Retrieves all documents from the Firestore, excluding any documents with the ID 'TEST'.
        :return: A list of dictionaries, each representing a document in the Firestore collection.
        :rtype: list of dict
        """

        result = self.cl.get()
        docs = [doc.to_dict() for doc in result if doc.exists and doc.id != 'TEST']
        return docs

    def getDocumentByDocCode(self, dc: str) -> dict | None:
        """
        :param dc: The unique document code used to identify the document.
        :type dc: str

        :return: The document data as a dictionary if the document exists, otherwise None.
        :rtype: dict or None
        """

        doc = self.cl.document(dc).get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def addDocument(self, doc: Document):
        """
        Adds a new document to the Firestore.

        :param doc: The document to be added to the Firestore collection.
        :type doc: Document
        """

        self.cl.document(doc.getDocCode()).set(doc.getDict())

    def removeDocument(self, dc: str):
        """
        Removes a document from the Firestore based on the provided document code (docCode).

        :param dc: The unique document code of the document to be removed.
        :type dc: str
        """

        self.cl.document(dc).delete()
