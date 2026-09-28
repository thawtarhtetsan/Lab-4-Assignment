def test_funded_account_has_initial_balance(funded_account):
    assert funded_account.balance == 1000


def test_funded_account_can_deposit(funded_account):
    funded_account.deposit(500)
    assert funded_account.balance == 1500
