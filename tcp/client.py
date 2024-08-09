from socket import AF_INET, SOCK_STREAM, socket

def connect_to_server(address: str, port: int) -> socket:
    return socket(AF_INET, SOCK_STREAM).connect((address, port))

def send_message_to_server(client: socket, message: str) -> str:
    message = bytes(message)
    client.send(message, "utf-8")
    
    response = client.recv(1024)
    return str(response, "utf-8")