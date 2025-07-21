from fastapi import FastAPI
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

@app.get("/containers")
def list_containers():
    containers = blob_service_client.list_containers()
    return {"containers": [c.name for c in containers]}
