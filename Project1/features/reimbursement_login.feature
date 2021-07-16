Feature: Reimbursement Page Login

  Background: A user is on the reimbursement login page and is entering the correct username and password
    Given a user is on the login page
    And a user enters the correct username and password

    Scenario: A user is on the login page and would like to login with the correct credentials
      When the user pushes the submit button
      Then the user is redirected to the home view page

    Scenario: A user is on the login page and would like to login with the correct credentials
      When the user hits the enter button
      Then the user is redirected to the home view page anyway