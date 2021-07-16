Feature: Reimbursement Page Login

  Background: A manager is on the reimbursement login page and is entering the correct username and password
    Given a manager is on the login page
    And a manager enters the correct username and password

    Scenario: A manager is on the login page and would like to login with the correct credentials
      When the manager pushes the submit button
      Then the manager is redirected to the home view page

    Scenario: A manager is on the login page and would like to login with the correct credentials
      When the manager hits the enter button
      Then the manager is redirected to the home view page anyway