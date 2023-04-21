import json


def hello(event, context):
    body = {
        "message": "Hello, everybody!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
