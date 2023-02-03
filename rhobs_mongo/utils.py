from pymongo import MongoClient
import json
import os


def get_mongo_client():
    """
        Returns a MongoClient instance using the credentials stored in a JSON file.

        Returns:
            pymongo.MongoClient: A MongoClient instance.
    """
    credentials_path = os.path.join(os.path.dirname(__file__), "mongo_credentials.json")
    with open(credentials_path, "r") as file:
        creds = json.load(file)
        return MongoClient(**creds)
