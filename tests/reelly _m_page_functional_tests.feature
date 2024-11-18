# Created by dchku at 11/5/2024
Feature: Tests for the main page

  Scenario: User can change the language from the page
    Given open the main page
    When Log in to the page
    And click on the menu
    And Change the language of the page to Russian
    Then Verify the language has changed