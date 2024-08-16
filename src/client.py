from socket import AF_INET, SOCK_STREAM, socket

from src.caesar_cypher import encrypt_using_caesar_cypher
from src.connection import receive_message, send_message
from src.diffie_hellman import (
    compute_shared_secret,
    generate_private_diffie_hellman_key,
    generate_public_diffie_hellman_key,
)


def start_client(host: str = "", port: int = 1300, bufsize: int = 1024):
    """Inicia uma conexão do cliente com o servidor.

    Args:
        host (str, optional): Endereço do servidor.
        port (int, optional): Porta aberta do servidor.
        bufsize (int, optional): Tamanho máximo de mensagem em bits.
    """

    address = (host, port)

    with socket(AF_INET, SOCK_STREAM) as client:
        client.connect(address)

        while True:
            diffie_hellman_params = receive_message(client, bufsize)
            p, g = _parse_diffie_hellman_params(diffie_hellman_params)
            private_key = generate_private_diffie_hellman_key(p)

            server_key = int(receive_message(client, bufsize))

            public_key = generate_public_diffie_hellman_key(p, g, private_key)
            send_message(client, public_key)

            secret = compute_shared_secret(p, private_key, server_key)

            message = input("Insira sua mensagem: ")
            message = encrypt_using_caesar_cypher(message, secret)

            send_message(client, message)


def _parse_diffie_hellman_params(params: str) -> tuple[int, int]:
    return tuple(int(i.strip()) for i in params.split(","))
