# import os
#
# import boto3
# from behave import given,when
#
#
# @given('My aws account is created')
# def aws_account(context):
#     context.client = boto3.client('lambda')
#
#
# @when('I create a Lambda function named "{function_name}"')
# def step_impl(context, function_name):
#     context.function_name = function_name
#     function_code_path = os.path.join(os.path.dirname(__file__), '../lambda_function_code.py')
#     with open(function_code_path, 'rb') as code_file:
#         function_code = code_file.read()
#     response = context.client.create_function(
#         FunctionName=function_name,
#         Runtime='python3.8',
#         Role='arn:aws:iam::997609234031:role/lambda-execution-role',
#         Handler='lambda_function.handler',
#         Code={
#             'ZipFile': function_code
#         },
#         Timeout=10,
#         MemorySize=128
#     )
#     context.function_arn = response['FunctionArn']
#
