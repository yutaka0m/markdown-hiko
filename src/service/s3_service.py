import logging
import os

import boto3
from botocore.exceptions import ClientError

from src.model.file_path import FilePath


class S3Service:
    """Service class of operates S3
    :param bucket: S3 bucket name
    """

    def __init__(self, bucket: str):
        # Check environment value
        if os.getenv("AWS_ACCESS_KEY_ID") is None:
            raise Exception("Please set AWS_SECRET_ACCESS_KEY")
        if os.getenv("AWS_SECRET_ACCESS_KEY") is None:
            raise Exception("Please set AWS_SECRET_ACCESS_KEY")
        if os.getenv("AWS_DEFAULT_REGION") is None:
            raise Exception("Please set AWS_DEFAULT_REGION")
        self.bucket = bucket

    def upload_file(self, file_path: FilePath, object_name=None) -> bool:
        """ Upload file to AWS S3

        :param file_path File path to upload to S3
        :param object_name　Name of file to save in S3
        :return True if upload is success
        """
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_path.get_file_name()

        # Upload the file
        s3_client = boto3.client("s3")
        try:
            s3_client.upload_file(file_path.value, self.bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
