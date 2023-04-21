import numb3rs

def test_valid_ip():
    """
    The function `test_valid_ip()` tests the `validate()` function of the `numb3rs` module for three
    different IP addresses.
    """
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("255.255.255.0") == True
    assert numb3rs.validate("0.0.0.0") == True

    """
    The function tests for invalid IP addresses using the numb3rs.validate() function.
    """
def test_invalid_ip():
    assert numb3rs.validate("256.0.0.0") == False
    assert numb3rs.validate("192.168.0") == False
    assert numb3rs.validate("192.168.0.1.2") == False
    assert numb3rs.validate("192.168.0.-1") == False
    assert numb3rs.validate("192.168.0.foo") == False
