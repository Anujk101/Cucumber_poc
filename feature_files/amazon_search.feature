Feature: Amazon Search 

    Scenario: Search for Amazon on Google
        Given On a Google search homepage
        When enter search term as Amazon.com
        Then click on a first link appear on search results 