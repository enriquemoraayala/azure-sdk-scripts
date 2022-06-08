import os, uuid
from threading import local
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
STORAGE = os.getenv('STORAGE')
TOKEN = os.getenv('TOKEN')

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    # Create a unique name for the container
    container_name = str(uuid.uuid4())

    local_file_name = 'rl4rs_benchmark_materials.tar.bz2'
    upload_file_path = '/Users/ESMoraEn/Downloads/' + local_file_name
    # Create the container
    container_client = blob_service_client.create_container(container_name)
    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)


except Exception as ex:
    print('Exception:')
    print(ex)


