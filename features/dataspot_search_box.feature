Feature: Check that the search box on the Dataspot website is working properly and I can search for products
  @T6 @positiveTesting
    Scenario Outline: Trying to search for a valid product that is listed on the website
      Given I am on the Dataspot homepage and I want to search for a valid product
      When I enter the "<product_name>" in the search box
      When I click the search button
      Then I am redirected to a new page that contains the "<results_message>"
      Examples:
      | product_name     | results_message  |
      | logitech         | rezultate pentru |
      | mouse            | rezultate pentru |
      | cleste sertizare | rezultate pentru |

  @T7 @negativeTesting
    Scenario: I am on the Dataspot homepage and I want to search for an invalid name product
      When I enter the invalid product name in the search box
      When I click the search button
      Then I am redirected to a new page with the following message displayed : "Nu sunt produse"