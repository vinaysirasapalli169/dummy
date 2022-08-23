
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import os, uuid
def home(name):
    res = []
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = ContainerClient.from_connection_string(connect_str,container_name="data")
    blob_list = blob_service_client.list_blobs()
    print(blob_service_client)
    print(blob_list)
    for blob in blob_list:
        
        temp = str(blob.name)
        folder,file = temp.split('/')
        print(folder,name)
        if folder  ==  name:
            res.append(file)
   
    return res


a = home('1')
print(a)



from flask import Flask
import os, uuid
from flask import jsonify
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


app = Flask(__name__)
app.route('/')
def hello(name = 1):
    res = []
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = ContainerClient.from_connection_string(connect_str,container_name="data")
    blob_list = blob_service_client.list_blobs()
    print(blob_service_client)
    print(blob_list)
    for blob in blob_list:
        temp = str(blob.name)
        folder,file = temp.split('/')
        print(folder,name)
        if folder  ==  name:
            res.append(file)
    return jsonify(res)