import json
import logging
import pytest
from aws_lambda_powertools.utilities.data_classes import S3Event
import handler

LOGGER = logging.getLogger(__name__)


@pytest.fixture()
def s3_single() -> S3Event:
    with open(f"fixtures/single.json") as f:
        return S3Event(json.load(f))


@pytest.fixture()
def s3_multiple() -> S3Event:
    with open(f"fixtures/multiple.json") as f:
        return S3Event(json.load(f))


def test_successful_single_object(s3_single: dict, caplog) -> None:
    handler.log(s3_single, "")
    assert "{'bucketName': 'mybucket', 'bucketKey': 'HappyFace.jpg'}" in caplog.text


def test_successful_multiple_object(s3_multiple: dict, caplog) -> None:
    handler.log(s3_multiple, "")
    assert "{'bucketName': 'mybucket', 'bucketKey': 'HappyFace.jpg'}" in caplog.text
    assert "{'bucketName': 'mybucket', 'bucketKey': 'HappyFace2.jpg'}" in caplog.text
