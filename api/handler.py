import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

SQS = boto3.client("sqs")

def get_queue_url():
    return os.getenv("QUEUE_URL")

def api(event, context):
    if not event.get("body"):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid Payload"})}

    try:
        SQS.send_message(
            QueueUrl=get_queue_url(),
            MessageBody=event["body"],
        )
    except Exception as e:
        logger.exception("Failed to queue message.")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Unable to process request."}),
        }

    return {"statusCode": 202, "body": json.dumps({"message": "Message Accepted"})}
