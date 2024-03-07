Feature: Check that the Sort By dropdown on the Dataspot website is working properly and I can sort the listed products
  @T8 @positiveTesting
  Scenario: Trying to sort the listed products by availability
    Given I am on the Dataspot website homepage, I want to see the laptops for sale and to sort them by availability
    When I click on the 'Calculatoare' category
    When I am redirected to the selected category page
    When I click on 'Laptop' option
    When I am redirected to the laptop products listed on the website
    When I select the Sort By dropdown
    When I click on the 'Disponibilitate' option
    Then The products are sorted by availability

  @T9 @positiveTesting
  Scenario: I am on the Dataspot website homepage, I want to see the laptops for sale and to sort them by ascending price
    When I select the Sort By dropdown
    When I click on the "Pret - crescator" option
    Then The products are sorted by ascending price

  @T10 @positiveTesting
  Scenario: I am on the Dataspot website homepage, I want to see the laptops for sale and to sort them by descending price
    When I select the Sort By dropdown
    When I click on the "Pret - descrescator" option
    Then The products are sorted by descending price

  @T11 @positiveTesting
  Scenario: I am on the Dataspot website homepage, I want to see the laptops for sale and to sort them by newest to oldest
    When I select the Sort By dropdown
    When I click on the "Cele mai noi" option
    Then The products are sorted by newest to oldest