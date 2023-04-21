import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        jar = Jar("abc")
    with pytest.raises(ValueError):
        jar = Jar(-5)
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_str():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.deposit("abc")
    with pytest.raises(ValueError):
        jar.deposit(-2)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(2)
    assert jar.size == 2

def test_withdraw():
    jar = Jar(4)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw("abc")
    with pytest.raises(ValueError):
        jar.withdraw(-2)
    with pytest.raises(ValueError):
        jar.withdraw(4)
    assert jar.size == 3
    jar.withdraw(2)
    assert jar.size == 1

def test_capacity():
    jar = Jar(8)
    assert jar.capacity == 8
    with pytest.raises(AttributeError):
        jar.capacity = 5

def test_size():
    jar = Jar(6)
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2
    with pytest.raises(AttributeError):
        jar.size = 3