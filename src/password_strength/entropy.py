import math


def estimate_entropy(password: str) -> float:
    # Shannon entropy estimation
    if not password:
        return 0.0
    freq = {char: password.count(char) for char in set(password)}
    length = len(password)
    return -sum((f / length) * math.log2(f / length) for f in freq.values()) * length
