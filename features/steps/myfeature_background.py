# from behave import given, when, then
#
# @given('the calculator is turned on')
# def turn_on_calculator(context):
#     # Perform actions to turn on the calculator (if necessary)
#     pass
#
# @given('I have entered {number:d} into the calculator')
# def enter_number(context, number):
#     context.number = number
#
# @given('I have also entered {number:d} into the calculator')
# def enter_other_number(context, number):
#     context.other_number = number
#
# @when('I press the addition button')  # Unique description
# def press_addition_button(context):
#     context.result = context.number + context.other_number
#
# @then('the result should be {expected_result:d} on the screen')
# def result(context, expected_result):
#     assert context.result == expected_result, f"Expected: {expected_result}, but got {context.result}"
