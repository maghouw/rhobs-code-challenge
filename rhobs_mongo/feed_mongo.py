from .utils import get_mongo_client
from tqdm import tqdm


def feed_mongo(database_name, collection_name, data_to_insert):
    """
        This function inserts a list of documents into a specified MongoDB collection.

        Args:
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        data_to_insert (list): A list of dictionaries representing the documents to be inserted.

        Returns:
        None
    """
    mongo_client = get_mongo_client()
    db = mongo_client.get_database(database_name)
    collection = db.get_collection(collection_name)
    for document in tqdm(
        data_to_insert, total=len(data_to_insert), desc="Inserting docs"
    ):
        collection.insert_one(document)
