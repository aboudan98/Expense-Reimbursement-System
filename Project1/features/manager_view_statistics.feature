Feature: Manager Statistic Page

  Scenario: A manager is viewing statistics page
    Given the manager is on the statistics page

  Scenario: The manager decides to go to home page
    When the manager hits the home button
    Then the manager redirected to the home page