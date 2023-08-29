import boto3
from behave import given,when,then


@given('I have an AWS account')
def aws_account(context):
    context.client = boto3.client('sns')


@when('I create an SNS topic with name "{topic_name}"')
def create_topic(context, topic_name):
    response = context.client.create_topic(Name=topic_name)
    context.my_topic_arn = response['TopicArn']


@then('the topic should exist in my AWS account')
def check_topic(context):
    result = context.client.list_topics()
    topics_list = [topic['TopicArn'] for topic in result['Topics']]
    assert context.my_topic_arn in topics_list, f"{context.my_topic_arn} does not exists in topics_list"


@when('I delete the SNS topic with name "my-topic"')
def delete_topic(context):
    response = context.client.delete_topic(TopicArn=context.my_topic_arn)


@then('the topic should not exist in my AWS account')
def check_for_del_topic(context):
    res = context.client.list_topics()
    topics_list = [topic['TopicArn'] for topic in res['Topics']]
    assert context.my_topic_arn not in topics_list, f"{context.my_topic_arn} exists in topics_list"


