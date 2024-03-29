import pymongo
import os

uri = os.environ.get("MONGO_DB_STRING").strip()


def get_user(cpf: str):

    client = pymongo.MongoClient(uri)
    db = client["fiap-lanches-client"]
    collection = db["cliente"]

    result = collection.find_one({"cpf": cpf})

    if result:
        return True
    else:
        return False
