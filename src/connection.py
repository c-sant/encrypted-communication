from socket import socket


def send_message(conn: socket, message):
    """Converte mensagem para bytes e envia.

    Args:
        conn (socket): Interface de conexão que enviará os dados.
        message (Any): Mensagem a ser enviada.
    """

    conn.sendall(str(message).encode())


def receive_message(conn: socket, bufsize: int) -> str:
    """Recebe mensagem e converte para string.

    Args:
        conn (socket): Interface de conexão que receberá os dados.
        bufsize (int): Quantidade máxima de dados.

    Returns:
        str: A mensagem recebida.
    """

    return str(conn.recv(bufsize), "utf-8")
