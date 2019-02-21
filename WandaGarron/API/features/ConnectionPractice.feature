# Created by ICSC at 2/20/2019
Feature: Test connection

  Scenario: My first connection
    Given I have connection to todo.ly
    When I get
    Then I receive status code 200