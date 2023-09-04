import boto3
from dotenv import load_dotenv
import os

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")


BUCKET_NAME = "sunbird-experimental-files"
DATA_FOLDER = "data/"

server = boto3.resource(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


class FileUploader:
    data_folder = DATA_FOLDER
    bucket_name = BUCKET_NAME

    def __init__(self, filename) -> None:
        self.key = filename

    def upload_file(self):
        file_path = f"{self.data_folder}/{self.key}.txt"
        server.Bucket(self.bucket_name).upload_file(file_path, self.key)

    def retrieve_file_url(self):
        return client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': self.bucket_name,
                'Key': self.key
            }
        )
