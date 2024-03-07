#Feature: Check that the Sort By dropdown on the Dataspot website search results page is working properly and I can sort the products
#  @T8 @positiveTesting
#    Scenario: Trying to sort the searched products by availability
#      Given I am on the Dataspot website search results page and I want to sort the products by availability
#      When I select the Sort By dropdown
#      When I click on the "Disponibilitate" option
#      Then The products are sorted by availability
#
#  @T9 @positiveTesting
#    Scenario: I am on the Dataspot website search results page and I want to sort the products by ascending price
#      When I select the Sort By dropdown
#      When I click on the "Pret - crescator" option
#      Then The products are sorted by ascending price
#
#  @T10 @positiveTesting
#    Scenario: I am on the Dataspot website search results page and I want to sort the products by descending price
#      When I select the Sort By dropdown
#      When I click on the "Pret - descrescator" option
#      Then The products are sorted by descending price
#
#  @T11 @positiveTesting
#    Scenario: I am on the Dataspot website search results page and I want to sort the products by newest to oldest
#      When I select the Sort By dropdown
#      When I click on the "Cele mai noi" option
#      Then The products are sorted by newest to oldest