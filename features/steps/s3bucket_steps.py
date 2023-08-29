from behave import given, when, then
import boto3


@given(u'Have an aws account')
def step_impl(context):
    context.client = boto3.client('s3')


@when(u'Create an s3 bucket with name "{bucket_name}"')
def step_impl(context, bucket_name):
    context.client.create_bucket(Bucket=bucket_name)
    context.created_bucket_name = bucket_name


@then(u'check if it exists in aws account')
def step_impl(context):
    response = context.client.list_buckets()
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]
    assert context.created_bucket_name in bucket_names, f"{context.created_bucket_name} is not found in bucket names"
