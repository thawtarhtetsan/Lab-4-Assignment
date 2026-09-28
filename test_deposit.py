import pytest
from bank import BankAccount

@pytest.fixture
def account():
    """Returns a fresh BankAccount with an initial balance of 100."""
    return BankAccount(100)

def test_deposit_increases_balance(account):
    """Test that depositing money increases the balance correctly."""
    account.deposit(50)
    assert account.balance == 150

def test_multiple_deposits(account):
    """Test that multiple consecutive deposits accumulate properly."""
    account.deposit(25)
    account.deposit(75)
    assert account.balance == 200
