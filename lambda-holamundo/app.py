def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hola Mundo desde AWS Lambda con SAM y CodePipeline!"
    }
