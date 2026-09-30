import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from fastapi import UploadFile

class StorageService:
    def __init__(self):
        self.endpoint = os.environ.get("S3_ENDPOINT", "http://seaweedfs:9000")
        self.access_key = os.environ.get("S3_ACCESS_KEY", "any")
        self.secret_key = os.environ.get("S3_SECRET_KEY", "any")
        self.bucket_name = os.environ.get("S3_BUCKET", "poc-bucket")

        self.s3_client = boto3.client(
            "s3",
            endpoint_url=self.endpoint,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            config=Config(signature_version="s3v4"),
        )
        
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        """Creates the bucket on startup if it doesn't already exist."""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
        except ClientError:
            self.s3_client.create_bucket(Bucket=self.bucket_name)

    def upload_file(self, file: UploadFile, object_name: str) -> str:
        """Uploads a FastAPI UploadFile to SeaweedFS."""
        try:
            self.s3_client.upload_fileobj(
                file.file, 
                self.bucket_name, 
                object_name,
                ExtraArgs={"ContentType": file.content_type}
            )
            # Return the URL to access the file
            return f"{self.endpoint}/{self.bucket_name}/{object_name}"
        except ClientError as e:
            print(f"Failed to upload {object_name}: {e}")
            raise

    def get_file_url(self, object_name: str) -> str:
        """Generates a presigned URL if you want private access, or returns direct URL."""
        return f"{self.endpoint}/{self.bucket_name}/{object_name}"


storage = StorageService()