from behave import given, when, then


@given('I have entered {number:d} into the calculator')
def enter_number(context, number):
    context.number = number


@given('I have also entered {number:d} into the calculator')
def enter_another_number(context, number):
    context.another_number = number


@when('I press add')
def add_numbers(context):
    context.result = context.number + context.another_number


@then('the result should be {expected_result:d} on the screen')
def result(context, expected_result):
    assert expected_result == context.result, f"Expected: {expected_result}, but got {context.result}"
