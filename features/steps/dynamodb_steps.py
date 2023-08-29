# # from behave import given, when, then
# # import boto3
# #
# #
# # @given('I have AWS account')
# # def aws_account(context):
# #     context.client = boto3.client('dynamodb')
# #     context.resource = boto3.resource('dynamodb')
# #
# #
# # @when('I create a DynamoDB table with name "{table_name}" and partition key "{partition_key_id}"')
# # def step_impl(context, table_name, partition_key_id):
# #     table = context.client.create_table(
# #         TableName=table_name,
# #         KeySchema=[
# #             {
# #                 'AttributeName': partition_key_id,
# #                 'KeyType': 'HASH'  # Partition_key
# #             }
# #         ],
# #         AttributeDefinitions=[
# #             {
# #                 'AttributeName': partition_key_id,
# #                 'AttributeType': 'N'
# #             }
# #         ],
# #         ProvisionedThroughput={
# #             'ReadCapacityUnits': 5,
# #             'WriteCapacityUnits': 5
# #         }
# #     )
# #
# #     context.table_name = table_name
# #
# #
# # @then('the table should exist in my AWS account')
# # def step_impl(context):
# #     table = context.table_name
# #     assert table.table_status == 'ACTIVE', f'{context.table_name} does not exists'
# #
# #
# # @when('I update the read capacity units to {updated_number} for table "{table_name}"')
# # def step_impl(context, updated_number, table_name):
# #     resp = context.client.update_table(
# #         TableName=table_name,
# #         ProvisionedThroughput={
# #             'ReadCapacityUnits': int(updated_number),
# #             'WriteCapacityUnits': 5,
# #         }
# #     )
# #
# #
# # @then(u'the table\'s read capacity units should be 10')
# # def step_impl(context):
# #     table = context.client.Table(context.table_name)
# #     context.table_description = table.table_status
# #     assert context.table_description['ProvisionedThroughput']['ReadCapacityUnits'] == 10, f"Given table doesn't " \
# #                                                                                           f"contain the " \
# #                                                                                           f"ReadCapacityUnits as " \
# #                                                                                           f"{context.updated_number}"
# from behave import given, when, then
# import boto3
#
#
# @given('I have AWS account')
# def aws_account(context):
#     context.client = boto3.client('dynamodb')
#     context.resource = boto3.resource('dynamodb')
#
#
# @when('I create a DynamoDB table with name "{table_name}" and partition key "{partition_key_id}"')
# def step_impl(context, table_name, partition_key_id):
#     # Check if the table already exists, and delete it if needed
#     existing_table = context.resource.Table(table_name)
#     if existing_table in context.resource.tables.all():
#         existing_table.delete()
#         existing_table.wait_until_not_exists()
#
#     # Create the DynamoDB table
#     table = context.resource.create_table(
#         TableName=table_name,
#         KeySchema=[
#             {
#                 'AttributeName': partition_key_id,
#                 'KeyType': 'HASH'
#             }
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': partition_key_id,
#                 'AttributeType': 'N'
#             }
#         ],
#         ProvisionedThroughput={
#             'ReadCapacityUnits': 5,
#             'WriteCapacityUnits': 5
#         }
#     )
#     table.wait_until_exists()
#
#     context.table_name = table_name
#
#
# @then('the table should exist in my AWS account')
# def step_impl(context):
#     table = context.resource.Table(context.table_name)
#     assert table.table_status == 'ACTIVE', f'{context.table_name} does not exist'
#
#
# @when('I update the read capacity units to {updated_number} for table "{table_name}"')
# def step_impl(context, updated_number, table_name):
#     table = context.resource.Table(table_name)
#     table.update(ProvisionedThroughput={'ReadCapacityUnits': int(updated_number), 'WriteCapacityUnits': 5})
#
#
# @then("the table's read capacity units should be 10")
# def step_impl(context):
#     import time
#
#     table = context.resource.Table(context.table_name)
#
#     # Wait for a brief moment before checking the read capacity units
#     time.sleep(5)
#
#     table.reload()
#     assert table.provisioned_throughput["ReadCapacityUnits"] == 10, f"Read capacity units are not 10"
