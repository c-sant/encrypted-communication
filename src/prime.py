import math
import random


def is_prime(number: int) -> bool:
    """Determina se um número é primo ou não.

    Args:
        n (int): Um candidato a número primo.

    Returns:
        bool: True se o número for primo; caso contrário, False.
    """

    if number <= 1:
        # 0 ou negativo
        return False

    if number <= 3:
        # 2 ou 3
        return True

    if number % 2 == 0:
        # número par
        return False

    for i in range(5, math.ceil(math.sqrt(number)), 2):
        if number % i == 0:
            return False

    return True


def generate_random_prime(bits: int = 1024) -> int:
    """Gera um número primo aleatório de um determinado tamanho.

    Args:
        bits (int, optional): Tamanho em bits do número gerado.

    Returns:
        int: Um número primo aleatório do tamanho especificado.
    """

    while True:
        # garante que seja ímpar ao utilizar a operação OR com o número 1
        n = random.getrandbits(bits) | 1

        if is_prime(n):
            return n
