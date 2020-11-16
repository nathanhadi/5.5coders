import boto3
from botocore.exceptions import ClientError


users_info_table_name = "users_readings_info"
client_name = "dynamodb"
endpoint_url = "http://localhost:8000"

def get_users_info_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(client_name, endpoint_url)
    table = dynamodb.Table(table_name)
    return table


######### GETTERS ###########

def get_readings(user_name, dynamodb=None):
    table = get_users_info_table()
    try:
        readings = table.get_item(Key={'user': user_name})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return readings

def get_reading(user_name, reading_name, dynamodb=None):
    table = get_users_info_table()
    try:
        reading = table.get_item(Key = {'user' : user_name,
                                         'reading_name' : reading_name})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return reading


########## ADDERS ##############

def add_reading_goal(user_name, reading_name, goal_name, goal_date):
    table = get_users_info_table()
    reading = table.update_item(Key = {'user' : user_name,
                                       'reading_name' : reading_name},
           UpdateExpression = "set goal.name=:goal_name, goal.date=:goal_date")
    return reading

def add_reading(user_name, email, password, reading_name,
                pages, chapters, tags, goal_name, goal_date, reminder_pref):
    table = get_users_info_table()
    reading = table.put_item(
               Item = {
                    'user' : user_name,
                    'email' : email,
                    'password' : password,
                    'reminder' : reminder_pref,
                    'reading_name' : reading_name,
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
