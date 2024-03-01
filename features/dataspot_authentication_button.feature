Feature: Check that the authentication button on the Dataspot website is working properly and I can access my account
  @T1 @negativeTesting
  Scenario Outline: Trying to authenticate with an invalid password
    Given I am on the Dataspot homepage and I want to authenticate with an invalid password
    When I click on authentication button
    When I enter the valid email address
    When I insert my invalid "<password>"
    When I click on sign in account button
    Then I receive an "<error_message>"
    Examples:
      | password  |error_message|
      | asdasdsa  |Autentificare esuata.|
      | sxvvvxc   |Autentificare esuata.|
      | undoitrei |Autentificare esuata.|

    @T2 @positiveTesting
  Scenario: I am on the Dataspot website homepage and I want to authenticate with the correct credentials
      When I click on authentication button
      When I enter my valid password
      When I click on the sign in account button
      Then I am redirected to my account page