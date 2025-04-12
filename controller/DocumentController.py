from datetime import datetime

from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from model.Document import Document
from service.DocumentService import DocumentService

from app_config.config import settings


class DocumentController:

    def __init__(self):
        self.service = DocumentService()
        self.router = APIRouter()
        self.router.add_api_route(settings.get_all_docs_url, self.getAllDocuments, methods=["GET"])
        self.router.add_api_route(settings.add_doc_url, self.addDocument, methods=["POST"])
        self.router.add_api_route(settings.delete_doc_url, self.deleteDocument, methods=["DELETE"])
        self.router.add_api_route(settings.get_doc_url, self.getDocument, methods=["POST"])

    async def getDocument(self, request: Request):
        """
        Retrieves a document from Firestore using the provided document code.
        The JSON body must contain the 'docCode' which uniquely identifies the document to be retrieved from Firestore.
        """

        try:

            body = await request.json()
            docCode = body.get('docCode')

            doc = self.service.getDocumentByDocCode(docCode)

            if doc is None:
                return JSONResponse({"alert": "There is no document !", "data": doc}, status_code=404)

            return JSONResponse({"message": "Successful !", "data": doc}, status_code=200)

        except Exception as e:
            print(e)
            return JSONResponse({"alert": "Error has occurred !"}, status_code=400)

    async def getAllDocuments(self):
        """
        Retrieves all documents from Firestore.
        """

        try:
            docs = self.service.getAllDocuments()

            if docs is None or len(docs) == 0:
                return JSONResponse({"alert": "There is no document !", "data": docs}, status_code=404)

            return JSONResponse({"message": "Successful !", "data": docs}, status_code=200)

        except Exception as e:
            print(e)
            return JSONResponse({"alert": "Error has occurred !"}, status_code=400)

    async def addDocument(self, request: Request):
        """
        Adds a new document to the database.

        The JSON body of the request must contain the following fields:
            - 'code': The document code.
            - 'firmName': The name of the firm associated with the document.
            - 'startDate': The start date of the document in 'YYYY-MM-DD' format.
            - 'endDate': The end date of the document in 'YYYY-MM-DD' format.
            - 'docNumber': The document number.
        """

        try:

            body = await request.json()

            code = body.get("code")
            firmName = body.get("firmName")
            startDate = datetime.strptime(body.get("startDate"), "%Y-%m-%d").date()
            endDate = datetime.strptime(body.get("endDate"), "%Y-%m-%d").date()
            docNumber = body.get("docNumber")

            if code == None or code == "": raise Exception("All fields are required !")
            if firmName == None or firmName == "": raise Exception("All fields are required !")
            if startDate == None or startDate == "": raise Exception("All fields are required !")
            if endDate == None or endDate == "": raise Exception("All fields are required !")
            if docNumber == None or docNumber == "": raise Exception("All fields are required !")

            newDocument = Document(code, firmName, startDate, endDate, docNumber)

            result = self.service.getDocumentByDocCode(newDocument.getDocCode())

            if result is not None:
                return JSONResponse({"message": "Document already exists !"}, status_code=406)

            self.service.addDocument(newDocument)
            return JSONResponse({"message": "A new document has been successfully added !"}, status_code=201)

        except Exception as e:
            print(e)
            return JSONResponse({"alert": "A new document cannot be added !"}, status_code=400)

    async def deleteDocument(self, request: Request):

        """
        Deletes a document from Firestore based on the provided document code.

        The JSON body of the request must contain the following field:
            - 'docCode': The unique code identifying the document to be deleted.
        """

        try:

            body = await request.json()

            docCode = body.get("docCode")

            doc = self.service.getDocumentByDocCode(docCode)

            if doc is None:
                return JSONResponse({"alert": "Document does not exist !"}, status_code=406)

            self.service.removeDocument(doc['DocCode'])
            return JSONResponse({"message": "Document has been deleted successfully !"}, status_code=200)

        except Exception as e:
            print(e)
            return JSONResponse({"alert": "Alert has occurred !"}, status_code=400)
