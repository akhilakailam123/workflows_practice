Feature: Calculator
    In order to perform arithmetic operations
    As a user
    I want to use the calculator

    Background:
        Given the calculator is turned on

    Scenario: Add two numbers
        Given I have entered 2 into the calculator
        And I have also entered 3 into the calculator
        When I press add
        Then the result should be 5 on the screen

    Scenario Outline: Add series of numbers
        Given I have entered <number1> into the calculator
        And I have also entered <number2> into the calculator
        When I press add
        Then The result should be <expected_result> on the screen
        Examples:
            | number1 | number2 | expected_result |
            | 3       | 5       | 8               |
            | 34      | 50      | 84              |
            | 20      | 5       | 25              |
