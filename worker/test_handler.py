from moto import mock_s3
import json
import boto3
import pytest
from aws_lambda_powertools.utilities.data_classes import SQSEvent
import handler


@pytest.fixture()
def sqs_single() -> SQSEvent:
    with open(f"fixtures/single.json") as f:
        return SQSEvent(json.load(f))


@pytest.fixture()
def sqs_multiple() -> SQSEvent:
    with open(f"fixtures/multiple.json") as f:
        return SQSEvent(json.load(f))


@mock_s3
def test_successful_single_event(sqs_single: dict, monkeypatch) -> None:
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket="test_bucket")
    monkeypatch.setenv("BUCKET_NAME", "test_bucket")
    handler.work(sqs_single, "")
    result = s3.get_object(Bucket="test_bucket", Key="events/MessageID_1.json")
    result_json = json.load(result["Body"])
    assert result_json["messageId"] == "MessageID_1"


@mock_s3
def test_successful_multiple_event(sqs_multiple: dict, monkeypatch) -> None:
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket="test_bucket")
    monkeypatch.setenv("BUCKET_NAME", "test_bucket")
    handler.work(sqs_multiple, "")
    result_one = s3.get_object(Bucket="test_bucket", Key="events/MessageID_1.json")
    result_one_json = json.load(result_one["Body"])
    result_two = s3.get_object(Bucket="test_bucket", Key="events/MessageID_2.json")
    result_two_json = json.load(result_two["Body"])

    assert result_one_json["messageId"] == "MessageID_1"
    assert result_two_json["messageId"] == "MessageID_2"
