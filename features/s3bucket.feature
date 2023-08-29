Feature: Creating an s3 bucket
  Scenario: Create an s3 bucket
    Given Have an aws account
    When Create an s3 bucket with name "my-test-bucket-bdd"
    Then check if it exists in aws account