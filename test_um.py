from um import count
"""
The function tests if the count function from the um module returns 0 when given an empty string as
input.
"""

def test_count_empty_string():
    assert count("") == 0