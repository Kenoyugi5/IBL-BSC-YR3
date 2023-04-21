import bank

def test_value_hello():
    """
    The function tests the value of a string input in a bank system and asserts that it should be equal
    to 0 for certain cases.
    """
    assert bank.value("hello world") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hello123") == 0

def test_value_h():
    """
    This function tests if the bank's value method returns 20 for the input "hi" or "Hi".
    """
    assert bank.value("hi") == 20
    assert bank.value("Hi") == 20