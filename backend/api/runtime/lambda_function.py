import json
import logging
import os
from dataclasses import asdict, dataclass

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = os.environ.get("BUCKET_NAME")
URL_TTL = os.environ.get("URL_TTL", 3600)
s3_client = boto3.client("s3")


@dataclass
class Response:
    """
    A class to represent a response.
    """

    statusCode: int
    body: str


def make_response(status_code: int, body: dict) -> dict:
    """
    Create a response dictionary.
    """

    return asdict(Response(statusCode=status_code, body=json.dumps(body)))


def generate_presigned_url(bucket_name: str, object_key: str) -> str:
    """
    Generate a presigned URL for uploading a file to S3.
    """

    try:
        response = s3_client.generate_presigned_url(
            "put_object",
            Params={"Bucket": bucket_name, "Key": object_key},
            ExpiresIn=URL_TTL,
        )
        return response
    except Exception as e:
        logger.exception(f"Error generating presigned URL: {e}")
        return None


def lambda_handler(event, context):
    """
    AWS Lambda function handler.
    """
    logger.info(f"Received event: {json.dumps(event)}")

    file_name = event.get("queryStringParameters", {}).get("file_name")
    if not file_name:
        logger.error("File name not provided in query string parameters.")
        return make_response(400, {"error": "File name is required."})
    if not file_name.endswith(".csv"):
        logger.error("Invalid file name provided.")
        return make_response(400, {"error": "File name must end with .csv."})
    object_key = f"uploads/{file_name}"
    presigned_url = generate_presigned_url(BUCKET_NAME, object_key)
    if not presigned_url:
        logger.error("Failed to generate presigned URL.")
        return make_response(500, {"error": "Failed to generate presigned URL."})
    logger.info(f"Generated presigned URL: {presigned_url}")
    response_body = {
        "presigned_url": presigned_url,
        "object_key": object_key,
    }
    logger.info(f"Response body: {response_body}")
    return make_response(200, response_body)
