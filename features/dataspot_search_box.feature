Feature: Check that the search box on the Dataspot website is working properly and I can search for products
  @T6 @positiveTesting
    Scenario Outline: Trying to search for a valid product that is listed on the website
      Given I am on the Dataspot homepage and I want to search for a valid product
      When I enter the "<product_name>" in the search box
      When I click the search button
      Then I am redirected to a new page that contains the "<results_message>"
      Examples:
      | product_name     | results_message  |
      | logitech         | rezultate        |
      | mouse            | rezultate        |
      | cleste           | rezultate        |

  @T7 @negativeTesting
    Scenario Outline: Trying to search for an invalid product that is not listed on the website
      Given I am on the Dataspot homepage and I want to search for an invalid product
      When I enter the "<invalid_product>" name in the search box
      When I click on the search button
      Then I am redirected to a new page with the following message displayed : "<no_results>"
      Examples:
      | invalid_product     | no_results      |
      | ^%#$#$#@$#@         | Nu sunt produse |
      | saltea matrimoniala | Nu sunt produse |
      | pulpe de pui        | Nu sunt produse |