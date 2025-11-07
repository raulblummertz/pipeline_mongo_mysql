from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import requests
load_dotenv()

db_password = os.getenv("DB_PASSWORD")
uri_mongo = f"mongodb+srv://raulblummertz:{db_password}@cluster-pipeline.jzk8vg0.mongodb.net/?appName=Cluster-pipeline"
url_api = os.getenv("API_URL")

def connect_mongo(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        return None
        
    
        
def create_connect_db(client, db_name):
    db = client[str(db_name)]
    print(db)
    return db

def create_connect_collection(db, collection_name):
    collection = db[collection_name]
    return collection

def  extract_api_data(url):
    return requests.get(url).json()

def insert_data(col, data):
    docs = col.insert_many(data)
    return len(docs.inserted_ids)

if __name__ == "__main__":
    
    client = connect_mongo(uri_mongo)
    db = create_connect_db(client, "db_produtos_desafio")
    col = create_connect_collection(db, "produtos")

    data = extract_api_data(url_api)
    print(f"\nQuantidade de dados extraidos: {len(data)}")

    n_docs = insert_data(col, data)
    print(f"\nDocumentos inseridos na colecao: {n_docs}")

    client.close()