import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def log(event, context):
    for record in event["Records"]:
        logger.info(
            {
                "bucketName": record["s3"]["bucket"]["name"],
                "bucketKey": record["s3"]["object"]["key"],
            }
        )
