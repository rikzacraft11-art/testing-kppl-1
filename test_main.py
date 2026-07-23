from main import is_even, is_odd


def test_is_even():
    assert is_even(2) is True
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(1) is False
    assert is_even(-3) is False


def test_is_odd():
    assert is_odd(1) is True
    assert is_odd(3) is True
    assert is_odd(-5) is True
    assert is_odd(2) is False
    assert is_odd(0) is False
