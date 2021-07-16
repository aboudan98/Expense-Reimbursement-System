Feature: User Reimbursement Page

  Scenario: A user is entering the reimbursement reason and amount
    Given the user on the reimbursement view page
    And the user enters the reimbursement reason and the user enters the reimbursement amount

  Scenario: The user wants to go back to the main page
    When the user hits the home page button
    Then the user redirected to the home page