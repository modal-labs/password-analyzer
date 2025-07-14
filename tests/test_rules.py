from src.password_strength.rules import (
    has_mixed_case,
    has_special_chars,
    has_min_length,
)


def test_has_mixed_case():
    assert has_mixed_case("Abc")
    assert not has_mixed_case("abc")
    assert not has_mixed_case("ABC")


def test_has_special_chars():
    assert has_special_chars("hello!")
    assert not has_special_chars("hello")


def test_has_min_length():
    assert has_min_length("abcdefgh")
    assert not has_min_length("abc")
