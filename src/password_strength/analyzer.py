from .rules import (
    has_mixed_case,
    has_special_chars,
    has_min_length,
)
from .entropy import estimate_entropy


def is_strong_password(password: str) -> bool:
    if not has_min_length(password, 8):
        return False
    if not has_mixed_case(password):
        return False
    if not has_special_chars(password):
        return False
    if estimate_entropy(password) < 40:
        return False
    return True
