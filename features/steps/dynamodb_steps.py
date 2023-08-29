# from behave import given, when, then
# import boto3
#
#
# @given(u'I have AWS account')
# def step_impl(context):
#     context.client = boto3.client('dynamodb')
#
#
# @when(u'I create a DynamoDB table with name "{table_name}" and partition key "{partition_key}"')
# def step_impl(context, table_name, partition_key):
#     context.table_name = table_name  # Corrected variable name
#     table = context.client.create_table(
#         TableName=table_name,
#         KeySchema=[
#             {
#                 'AttributeName': partition_key,
#                 'KeyType': 'HASH'  # Partition_key
#             }
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': partition_key,
#                 'AttributeType': 'N'  # Corrected data type to 'N' for numeric
#             }
#         ],
#         ProvisionedThroughput={
#             'ReadCapacityUnits': 5,
#             'WriteCapacityUnits': 5
#         }
#     )
#     context.client.get_waiter('table_exists').wait(TableName=table_name)
#
#
# @then(u'the table should exist in my AWS account')
# def step_impl(context):
#     existing_tables = context.client.list_tables()['TableNames']
#     assert context.table_name in existing_tables, f"{context.table_name} doesn't exist in AWS account"
#
#
# @when(u'I update the read capacity units to 2 for table "{table_name}"')
# def step_impl(context, table_name):
#     context.client.update_table(
#         TableName=table_name,
#         ProvisionedThroughput={
#             'ReadCapacityUnits': 2,
#             'WriteCapacityUnits': 5  # You can also update WriteCapacityUnits if needed
#         }
#     )
#
#
# @then(u'the table\'s read capacity units should be 2')
# def step_impl(context):
#
#     response = context.client.describe_table(TableName=context.table_name)
#     table_description = response['Table']
#
#     current_read_capacity_units = table_description['ProvisionedThroughput']['ReadCapacityUnits']
#
#     # Assert that the current read capacity units are equal to 4
#     assert current_read_capacity_units == 2, f"Expected read capacity units: 2, Actual: {current_read_capacity_units}"

# Import necessary libraries
from behave import given, when, then
import boto3
from botocore.exceptions import ClientError

# Define a global variable for the DynamoDB client
dynamodb_client = None


# Step 1: Set up AWS account
@given(u'I have AWS account')
def step_impl(context):
    # Create a DynamoDB client
    global dynamodb_client
    dynamodb_client = boto3.client('dynamodb')


# Step 2: Create a DynamoDB table
@when(u'I create a DynamoDB table with name "{table_name}" and partition key "{partition_key}"')
def step_impl(context, table_name, partition_key):
    try:
        response = dynamodb_client.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': partition_key,
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': partition_key,
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except ClientError as e:
        # Handle any exceptions that may occur during table creation
        context.table_creation_error = str(e)


# Step 3: Check if the table exists
@then(u'the table should exist in my AWS account')
def step_impl(context):
    # Check if an error occurred during table creation
    if hasattr(context, 'table_creation_error'):
        raise AssertionError(f"Table creation error: {context.table_creation_error}")

    # Wait for the table to become 'ACTIVE'
    table_name = context.table_name
    dynamodb_client.get_waiter('table_exists').wait(TableName=table_name)

    # List the tables and check if the created table is in the list
    existing_tables = dynamodb_client.list_tables()['TableNames']
    assert table_name in existing_tables, f"{table_name} doesn't exist in AWS account"


# Step 4: Update the read capacity units
@when(u'I update the read capacity units to 2 for table "{table_name}"')
def step_impl(context, table_name):
    try:
        dynamodb_client.update_table(
            TableName=table_name,
            ProvisionedThroughput={
                'ReadCapacityUnits': 2,
                'WriteCapacityUnits': 5
            }
        )
    except ClientError as e:
        context.update_error = str(e)


# Step 5: Check the updated read capacity units
@then(u'the table\'s read capacity units should be 2')
def step_impl(context):
    # Check if an error occurred during the update
    if hasattr(context, 'update_error'):
        raise AssertionError(f"Update error: {context.update_error}")

    # Describe the table to get its current provisioned throughput settings
    table_name = context.table_name
    response = dynamodb_client.describe_table(TableName=table_name)
    table_description = response['Table']
    current_read_capacity_units = table_description['ProvisionedThroughput']['ReadCapacityUnits']

    assert current_read_capacity_units == 2, f"Expected read capacity units: 2, Actual: {current_read_capacity_units}"
