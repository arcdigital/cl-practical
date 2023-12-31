import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

S3 = boto3.client("s3")

def get_bucket_name():
    return os.getenv("BUCKET_NAME")

def work(event, context):
    if event:
        failures = []
        response = {}

        for record in event["Records"]:
            logger.info(f"SQS Event: {record}")
            try:
                fileName = record["messageId"] + ".json"
                file = open(f"/tmp/{fileName}", "w")
                json.dump(record, file)
                file.close()
                S3.upload_file(f"/tmp/{fileName}", get_bucket_name(), f"events/{fileName}")
                os.remove(f"/tmp/{fileName}")
            except Exception as e:
                logger.exception(f"Failed to store event: {record['messageId']}")
                # append message id to failure array
                failures.append({"itemIdentifier": record['messageId']})
        
        # respond with any message ids in the batch that failed
        return response
