from compare import expect


@given(u'I have ${balance:d} in my account')
def step_impl(context, balance):
    context.balance = balance


@when(u'I choose to withdraw the fixed amount of ${withdraw:d}')
def step_impl(context, withdraw):
    context.withdraw = withdraw


@then(u'I should receive ${cash:d} cash')
def step_impl(context, cash):
    context.cash = cash
    print("This is your $", context.cash)


@then(u'the balance of my account should be ${balance:d}')
def step_impl(context, balance):
    remaining = context.balance - context.withdraw
    expect(remaining).to_equal(balance)

