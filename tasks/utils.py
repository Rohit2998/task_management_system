import boto3
import os
import json
from django.conf import settings

def trigger_lambda(task):
    lambda_client = boto3.client('lambda', region_name=settings.AWS_REGION)
    payload = json.dumps({"task_title": task.title, "assigned_to": task.assigned_to.username})    
    response = lambda_client.invoke(
        FunctionName=settings.AWS_LAMBDA_NAME,
        InvocationType="Event",
        Payload=payload
    )
    print(f"Lambda invoked: {response}")