from src.password_strength.entropy import estimate_entropy


def test_entropy_increases():
    assert estimate_entropy("aaaa") < estimate_entropy("abcd")
    assert estimate_entropy("abcd") < estimate_entropy("abcd1234")
    assert estimate_entropy("") == 0.0
