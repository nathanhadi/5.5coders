import boto3
from botocore.exceptions import ClientError
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr

access_key = "AKIA35XVUTN4TI7KDUU6"
secret_key = "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"
region = "us-east-1"
table_name = "User_Details"

def get_preferences(user_name):
    dynamodb_session = Session(aws_access_key_id=access_key,
          aws_secret_access_key=secret_key,
          region_name=region)
    dynamodb = dynamodb_session.resource('dynamodb')
    table=dynamodb.Table("User_Details")
    response = table.query(
        KeyConditionExpression=Key('Username').eq(user_name)
    )
    return response['Items']

def get_readings(user_name):
    dynamodb_session = Session(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region)

    dynamodb = dynamodb_session.resource('dynamodb')
    table=dynamodb.Table("Readings")

    response = table.query(
        KeyConditionExpression=Key('Username').eq(user_name)
    )
    return response['Items']

def get_reading(user_name, reading_name):
    readings = get_readings(user_name)
    return(list(filter(lambda book: book['Title'] == reading_name, readings)))

########## ADDERS ##############

def add_reading_goal(user_name, reading_name, goal_name, goal_date):
    dynamodb_session = Session(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region)

    dynamodb = dynamodb_session.resource('dynamodb')
    table=dynamodb.Table("Readings")
    
    reading = table.update_item(Key = {'user' : user_name,
                                       'title' : reading_name},
            UpdateExpression = "set goal.name=:n, goal.date=:d",
            ExpressionAttributeValues={
                ':n': goal_name,
                ':d': goal_date
            })
    return reading

def add_preferences(user_name, email, password, reminder_pref):
    dynamodb_session = Session(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region)

    dynamodb = dynamodb_session.resource('dynamodb')
    table=dynamodb.Table("User_Details")
    
    preference = table.put_item(
               Item = {
                    'user' : user_name,
                    'email' : email,
                    'password' : password,
                    'reminder' : reminder_pref,
                }
            )
    return preference

def add_reading(user_name, reading_name, pages, chapters, goal_name, goal_date):
    dynamodb_session = Session(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region)

    dynamodb = dynamodb_session.resource('dynamodb')
    table=dynamodb.Table("Readings")
    
    reading = table.put_item(
               Item = {
                    'user' : user_name,
                    'title' : reading_name,
                    'pages' : pages,
                    'chapters' : chapters,
                    'goal' : {
                        'name' : goal_name,
                        'date' : goal_date
                    }
                }
            )
    return reading
