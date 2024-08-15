def encrypt_using_caesar_cypher(message: str, offset: int) -> str:
    """Encripta mensagem utilizando cifra de César.

    Args:
        message (str): Mensagem que deve ser convertida.
        offset (int): Deslocamento utilizado.

    Returns:
        str: A mensagem convertida pela cifra de César.
    """

    return "".join([chr(ord(c) + offset) for c in message])
