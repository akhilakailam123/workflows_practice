#Feature: Create and update dynamodb table
#  Scenario: Create and Update DynamoDB Table
#    Given I have AWS account
#    When I create a DynamoDB table with name "my-table-for-bdd" and partition key "id"
#    Then the table should exist in my AWS account
#    When I update the read capacity units to 10 for table "my-table"
#    Then the table's read capacity units should be 10