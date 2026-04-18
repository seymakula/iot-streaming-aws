import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('iot-sensor-data')

def lambda_handler(event, context):
    print("Gelen veri:", json.dumps(event))
    
    table.put_item(Item={
        'device_id': event['device_id'],
        'timestamp': event['timestamp'],
        'temperature': str(event['temperature']),
        'humidity': str(event['humidity']),
        'pressure': str(event['pressure'])
    })
    
    print("DynamoDB'ye kaydedildi!")
    return {'statusCode': 200}
