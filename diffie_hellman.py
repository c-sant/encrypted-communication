def diffie_hellman(g: int, n: int, factor: int) -> int:
    return (g ** factor) % n