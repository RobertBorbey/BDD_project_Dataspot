Feature: Check that the registration button on the Dataspot website is working properly and I can create a new account

   @T4 @negativeTesting
     Scenario Outline: Trying to authenticate with an invalid name
      Given I am on the Dataspot homepage and I want to register with an invalid lastname and firstname
      When I click on the auth button
      When I click on the registration button
      When I insert an invalid "<name_surname>"
      When I enter a valid email address
      When I enter a random password
      When I click on the create account button
      Then An "<error_name_msg>" is displayed
      Examples:
      | name_surname       | error_name_msg |
      | Szccx*%^@%#_34     | Format nevalid.|
      | 1234_asgdeaszvb    | Format nevalid.|
      | ASDC2345_^&Smsd    | Format nevalid.|

   @T5 @positiveTesting
     Scenario: I am on the Dataspot homepage and I want to register with valid credentials
      When The authentication button is clicked
      When I click on the registration button
      When I fill the first field with a valid name
      When A valid email address is entered
      When I enter a random password
      When I click the create account button
      Then I am redirected to the Dataspot homepage, while connected to my new account