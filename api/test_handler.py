from moto import mock_sqs
import json
import boto3
import pytest
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
import handler


@pytest.fixture()
def apigw_valid() -> APIGatewayProxyEvent:
    with open(f"fixtures/valid.json") as f:
        return APIGatewayProxyEvent(json.load(f))


@pytest.fixture()
def apigw_invalid() -> APIGatewayProxyEvent:
    with open(f"fixtures/invalid.json") as f:
        return APIGatewayProxyEvent(json.load(f))


@mock_sqs
def test_successful_request_queue(apigw_valid: dict, monkeypatch) -> None:
    sqs = boto3.resource("sqs")
    queue = sqs.create_queue(QueueName="test-queue")
    monkeypatch.setenv("QUEUE_URL", queue.url)
    test_response = handler.api(apigw_valid, "")
    sqs_messages = queue.receive_messages()

    assert sqs_messages[0].body == apigw_valid["body"]
    assert test_response["statusCode"] == 202


@mock_sqs
def test_empty_body_fails(apigw_invalid: dict, monkeypatch) -> None:
    sqs = boto3.resource("sqs")
    queue = sqs.create_queue(QueueName="test-queue")
    monkeypatch.setenv("QUEUE_URL", queue.url)
    test_response = handler.api(apigw_invalid, "")
    assert test_response["statusCode"] == 400
