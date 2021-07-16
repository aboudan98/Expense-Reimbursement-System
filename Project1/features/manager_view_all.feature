Feature: Manager Reimbursement Page

  Scenario: A manager is viewing all reimbursement requests
    Given the manager is on the view all reimbursement requests

  Scenario: The manager decides to sign out
    When the manager hits the sign out button
    Then the manager redirected to the login page