Feature: Calculator
    In order to perform arithmetic operations
    As a user
    I want to use the calculator

    Scenario: Add two numbers
        Given I have entered 2 into the calculator
        And I have also entered 3 into the calculator
        When I press add
        Then the result should be 5 on the screen

    Scenario Outline: Add two numbers
        Given I have entered <number1> into the calculator
        And I have also entered <number2> into the calculator
        When I press add
        Then the result should be <expected_result> on the screen

        Examples:
        | number1 | number2 | expected_result |
        | 2       | 3       | 5               |
        | 5       | 7       | 12              |
        | 10      | 0       | 10              |

