import boto3
from botocore.exceptions import ClientError
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr

access_key = "AKIA35XVUTN4TI7KDUU6"
secret_key = "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"
region = "us-east-1"
table_name = "User_Details"
users_info_table_name = "users_readings_info"
client_name = "dynamodb"
endpoint_url = "http://localhost:8000"

# def get_users_info_table(dynamodb=None):
#     if not dynamodb:
#         dynamodb = boto3.resource(client_name, endpoint_url)
#     table = dynamodb.Table(table_name)
#     return table

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


# def get_readings(user_name, dynamodb=None):
#     table = get_users_info_table()
#     try:
#         readings = table.get_item(Key={'user': user_name})
#     except ClientError as e:
#         print(e.response['Error']['Message'])
#     else:
#         return readings

# def get_reading(user_name, reading_name, dynamodb=None):
#     table = get_users_info_table()
#     try:
#         reading = table.get_item(Key = {'user' : user_name,
#                                          'reading_name' : reading_name})
#     except ClientError as e:
#         print(e.response['Error']['Message'])
#     else:
#         return reading


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

def add_reading(user_name, email, password, reading_name,
                pages, chapters, tags, goal_name, goal_date, reminder_pref):
    dynamodb_session = Session(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region)

    dynamodb = dynamodb_session.resource('dynamodb')
    table=dynamodb.Table("Readings")
    
    reading = table.put_item(
               Item = {
                    'user' : user_name,
                    'title' : reading_name,
                    'email' : email,
                    'password' : password,
                    'reminder' : reminder_pref,
                    'pages' : pages,
                    'chapters' : chapters,
                    'tags' : tags,
                    'goal' : {
                        'name' : goal_name,
                        'date' : goal_date
                    }
                }
            )
    return reading
