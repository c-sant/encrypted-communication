from socket import AF_INET, SOCK_STREAM, socket

from src.caesar_cypher import encrypt_using_caesar_cypher
from src.connection import receive_message, send_message
from src.diffie_hellman import (
    compute_shared_secret,
    generate_private_diffie_hellman_key,
    generate_public_diffie_hellman_key,
    generate_public_diffie_hellman_parameters,
)


def start_server(
    host: str = "", port: int = 1300, backlog: int = 5, bufsize: int = 1024
):
    """Inicia o servidor TCP.

    Args:
        host (str, optional): O endereço IP do servidor.
        port (int, optional): A porta do servidor.
        backlog (int, optional): Número máximo de requisições por conexão.
        bufsize (int, optional): Tamanho máximo de mensagem em bits.
    """

    address = (host, port)

    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind(address)
        server.listen(backlog)

        conn, _ = server.accept()

        print(f"Started server at port {port}.")

        with conn:

            while True:
                p, g = generate_public_diffie_hellman_parameters()
                send_message(conn, f"{p}, {g}")
                
                private_key = generate_private_diffie_hellman_key(p)
                public_key = generate_public_diffie_hellman_key(p, g, private_key)
                send_message(conn, public_key)

                client_key = int(receive_message(conn, bufsize))

                secret = compute_shared_secret(p, private_key, client_key)

                message = receive_message(conn, bufsize)
                message = encrypt_using_caesar_cypher(message, -secret)

                print(f"Mensagem recebida: {message}")
