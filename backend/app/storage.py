import boto3
import uuid
from fastapi import UploadFile

s3_client = boto3.client(
    "s3",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    endpoint_url="http://s3:9000"
)

BUCKET_NAME = "voice-storage"

def upload_file_to_s3(file: UploadFile):
    s3_key = f"{uuid.uuid4()}_{file.filename}"
    s3_client.upload_fileobj(file.file, BUCKET_NAME, s3_key)
    return s3_key

def get_s3_file_url(s3_key: str):
    url = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET_NAME, "Key": s3_key},
        ExpiresIn=3600
    )
    return url

