from src.password_strength.analyzer import is_strong_password


def test_is_strong_password():
    assert is_strong_password("S3cure@Passw0rd")
    assert not is_strong_password("password")
    assert not is_strong_password("12345678")
    assert not is_strong_password("NoSpecial123")
    assert not is_strong_password("short1!")
