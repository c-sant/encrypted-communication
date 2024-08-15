import random

from src.prime import generate_random_prime


def generate_public_diffie_hellman_parameters() -> tuple[int, int]:
    """Gera os parâmetros públicos usadas pelo algoritmo Diffie-Hellman.

    Returns:
        tuple[int, int]: Os parâmetros públicos.
    """

    # p = generate_random_prime(1024) # ideal, mas muito lento
    p = 23
    g = 5

    return p, g


def generate_private_diffie_hellman_key(p: int) -> int:
    """Gera chave secreta usada para a troca de chaves de Diffie-Hellman.

    Args:
        p (int): Primeiro parâmetro de Diffie-Hellman.

    Returns:
        int: A chave privada deste dispositivo usada na troca de Diffie-Hellman.
    """

    return random.randint(1, p - 1)


def generate_public_diffie_hellman_key(p: int, g: int, private_key: int) -> int:
    """Gera chave pública usada para a troca de chaves de Diffie-Hellman.

    Args:
        p (int): Primeiro parâmetro de Diffie-Hellman.
        g (int): Segundo parâmetro de Diffie-Hellman.
        private_key (int): A chave privada deste dispositivo.

    Returns:
        int: A chave pública usada na troca de Diffie-Hellman.
    """

    return g**private_key % p


def compute_shared_secret(p: int, private_key: int, other_public_key: int) -> int:
    """Calcula o valor da chave para encriptar a mensagem.

    Args:
        p (int): Primeiro parâmetro de Diffie-Hellman.
        private_key (int): A chave privada deste dispositvo.
        other_public_key (int): A chave pública enviada pelo outro dispositivo.

    Returns:
        int: A chave usada para encriptar a mensagem.
    """

    return other_public_key**private_key % p
