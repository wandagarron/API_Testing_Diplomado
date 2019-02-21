@given(u'I am in the new gmail account page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am in the new gmail account page')


@given(u'my name is {name:s}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my name is {name:s}')


@given(u'my last name is {lastName:s}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my last name is {lastName:s}')


@given(u'my username is {userName:S}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my username is {userName:S}')


@given(u'my password is {password:S}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my password is {password:S}')


@given(u'my verification password is {verificationPassword:S}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my verification password is {verificationPassword:S}')


@given(u'the day of my birthday is {day:d}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the day of my birthday is {day:d}')


@given(u'the month of my birthday is {month:S}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the month of my birthday is {month:S}')


@given(u'the year of my birthday is {year:d}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the year of my birthday is {year:d}')


@given(u'my gender is {gender:S}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my gender is {gender:S}')


@given(u'my mobile phone country is {country:S}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my mobile phone country is {country:S}')


@given(u'my phone number is {phone:d}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my phone number is {phone:d}')


@given(u'my current email address is {currentAddress:S}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given my current email address is {currentAddress:S}')


@when(u'I press enter in the current email address')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press enter in the current email address')


@then(u'My account should be created successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then My account should be created successfully')


@then(u'An error the username already exist is shown')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then An error the username already exist is shown')


@then(u'An error the password and verification password does not match')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then An error the password and verification password does not match')
