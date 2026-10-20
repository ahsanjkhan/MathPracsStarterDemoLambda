import json
import os
from typing import Dict, Union

import boto3
from aws_lambda_typing import context as lambda_context

s3_client = boto3.client('s3')


def lambda_handler(event: Dict[str, Union[str, int, float, bool, None]], context: lambda_context.Context) -> Dict[str, Union[str, int]]:
    try:
        print(f"Received Event: {event}")

        bucket_name = os.environ['BUCKET_NAME']
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        file_names = [s3_object['Key'] for s3_object in response.get('Contents', [])]

        result = {
            'bucket': bucket_name,
            'count': len(file_names),
            'files': file_names
        }
        print(json.dumps(result))

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
