#Feature: Check that the search box on the Dataspot website is working properly and I can search for products
#  @T6 @positiveTesting
#    Scenario: Trying to search for a valid product that is listed on the website
#      Given I am on the Dataspot homepage and I want to search for a valid product
#      When I enter the valid product name in the search box
#      When I click the search button
#      Then I am redirected to a new page that contains the searched products as results
#
#  @T7 @negativeTesting
#    Scenario: Trying to search for an invalid product
#      Given I am on the Dataspot homepage and I want to search for an invalid product
#      When I enter the invalid product name in the search box
#      When I click the search button
#      Then I am redirected to a new page with the following message displayed : "Nu sunt produse"