"""
Database Services for Localization Management Bot.

Classes

    DatabaseService -- The implementation class of this module.
    
"""

import os
import tempfile

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class DatabaseService:
    """
    Class to handle database services

    Methods
    ---

    """
    def __init__(self) -> None:
        # Creating a temporary file for Firebase Admin Credential key
        config_json = tempfile.NamedTemporaryFile(delete=False,
                                                  dir="./",
                                                  encoding="utf-8",
                                                  mode="w+")
        try:
            # Write credential key from config/env file
            config_json.write(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

            # Seek to start and read the file
            config_json.seek(0)
            cred = credentials.Certificate(cert=config_json.name)

            # Initialize the app and client using the created credential
            self._app = firebase_admin.initialize_app(credential=cred)
            self.firestore_client = firestore.client(app=self._app)
        finally:
            config_json.close()
            os.unlink(config_json.name)

    # TODO: implement services


if __name__ == "__main__":
    service = DatabaseService()
