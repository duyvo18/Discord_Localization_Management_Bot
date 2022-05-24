"""
Database Services for Localization Management Bot.

Classes

    DatabaseService -- The implementation class of this module.
    
"""

import os
import tempfile
import asyncio

import firebase_admin
from firebase_admin import firestore
import google.cloud.firestore as firestore

from config_reader import ConfigReader

class DatabaseService:
    """
    Class to handle database services

    Methods
    ---

    """

    def __init__(self) -> None:
        # Creating a temporary file for Firebase Admin Credential key
        config_json = tempfile.NamedTemporaryFile(
            delete=False, dir="./", encoding="utf-8", mode="w+"
        )

        try:
            # Write credential key from config/env file
            config_json.write(
                ConfigReader.get_config(
                    section="Tokens", key="google_credentials"
                )
            )

            # Seek to start and read the file for Certificate
            config_json.seek(0)
            cred: firebase_admin.credentials.Certificate = firebase_admin.credentials.Certificate(
                cert=config_json.name
            )

            # Initialize the app and client using the created credential
            self._app: firebase_admin.App = firebase_admin.initialize_app(
                credential=cred
            )
            self.firestore_client: firestore.Client = firebase_admin.firestore.client(
                app=self._app
            )

        finally:
            config_json.close()
            os.unlink(config_json.name)

        if not self._app:
            # TODO: Print warning failed init
            pass

    def getDocument(self, docPath: str) -> firestore.DocumentReference:
        '''
        Get reference to a document.

        Parameters:
        ---
            *docPath (:class:`str`):
                A '/' delimited direct path to the document.

        Returns:
        ---
            :class:`firestore.DocumentReference`:
                Reference of the specified document.

        Raises:
        ---
            None.

        '''
        return self.firestore_client.document(docPath)

    async def setDocument(self, docRef: firestore.DocumentReference, data: dict) -> firestore.types.WriteResult:
        '''
        Async function to create or update a document.

        Parameters:
        ---
            docRef (:class:`firestore.DocumentReference`):
                A reference to a document.

            data (:class:`dict`):
                A key-value dictionary.

                The function will overwrite the existing data (if any)
                with this value.

        Returns:
        ---
            :class:`firestore.types.WriteResult`.
                The result object of the operation.

        Raises:
        ---
            None.

        '''
        result: firestore.types.WriteResult = docRef.set(document_data=data)
        return result


async def main():
    service = DatabaseService()
    doc = service.getDocument("test/testDoc")
    result = await service.setDocument(doc, {"key": "value"})
    print(result.update_time)


if __name__ == "__main__":
    asyncio.run(main())
