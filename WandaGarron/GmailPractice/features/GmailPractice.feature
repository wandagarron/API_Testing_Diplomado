Feature: Create account

Scenario: Create a new gmail account
  Given I am in the new gmail account page
    And my name is {name:s}
    And my last name is {lastName:s}
    And my username is {userName:S}
    And my password is {password:S}
    And my verification password is {verificationPassword:S}
    And the day of my birthday is {day:d}
    And the month of my birthday is {month:S}
    And the year of my birthday is {year:d}
    And my gender is {gender:S}
    And my mobile phone country is {country:S}
    And my phone number is {phone:d}
    And my current email address is {currentAddress:S}
  When I press enter in the current email address
  Then My account should be created successfully

  Scenario: The username in creation of a new gmail account already exist
   Given I am in the new gmail account page
    And my name is {name:s}
    And my last name is {lastName:s}
    And my username is {userName:S}
    And my password is {password:S}
    And my verification password is {verificationPassword:S}
    And the day of my birthday is {day:d}
    And the month of my birthday is {month:S}
    And the year of my birthday is {year:d}
    And my gender is {gender:S}
    And my mobile phone country is {country:S}
    And my phone number is {phone:d}
    And my current email address is {currentAddress:S}
  When I press enter in the current email address
  Then An error the username already exist is shown

  Scenario: The password verification in creation of a new gmail account is incorrect
   Given I am in the new gmail account page
    And my name is {name:s}
    And my last name is {lastName:s}
    And my username is {userName:S}
    And my password is {password:S}
    And my verification password is {verificationPassword:S}
    And the day of my birthday is {day:d}
    And the month of my birthday is {month:S}
    And the year of my birthday is {year:d}
    And my gender is {gender:S}
    And my mobile phone country is {country:S}
    And my phone number is {phone:d}
    And my current email address is {currentAddress:S}
  When I press enter in the current email address
  Then An error the password and verification password does not match