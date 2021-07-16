Feature: User Reimbursement Page

  Scenario: A user is viewing all reimbursement requests
    Given the user is on the view all reimbursement requests

  Scenario: The user decides to sign out
    When the user hits the sign out button
    Then the user redirected to the login page