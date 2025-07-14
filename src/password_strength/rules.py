def has_mixed_case(password: str) -> bool:
    return any(c.islower() for c in password) and any(c.isupper() for c in password)


def has_special_chars(password: str) -> bool:
    special = set("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`")
    return any(c in special for c in password)


def has_min_length(password: str, min_length: int = 8) -> bool:
    return len(password) >= min_length
