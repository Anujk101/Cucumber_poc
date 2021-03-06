from pytest_bdd import given, when, then


@given('On a Google search homepage')
def step_def():
    print('In Given')


@when('enter search term as Amazon.com')
def step_def():
    print('In when')


@then('click on a first link appear on search results')
def step_def():
    print('In Then')
