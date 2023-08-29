Feature: Create and Delete sns topic
  Scenario: Create and Delete an SNS Topic
    Given I have an AWS account
    When I create an SNS topic with name "my-topic"
    Then the topic should exist in my AWS account
    When I delete the SNS topic with name "my-topic"
    Then the topic should not exist in my AWS account