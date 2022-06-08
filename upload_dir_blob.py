import os
from upload_dir_blob import DirectoryClient
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')

local_path = "/home/azureuser/cloudfiles/code/Users/Enrique.Mora/rl4rs_data/rl4rs_benchmark_materials"
CONTAINER_NAME = "2f9d0748-1f42-457c-aad0-54945a8a8be2"

client = DirectoryClient(CONNECTION_STRING, CONTAINER_NAME)
client.upload_dir(local_path, 'rl4rs')
