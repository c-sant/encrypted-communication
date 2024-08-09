from socket import socket
from tcp import send_message_to_server, connect_to_server
from caesar_cypher import CaesarCypher
from diffie_hellman import diffie_hellman
import random

# Configurações

SERVER_ADDRESS = ""
SERVER_PORT = 1300
PRINT_RESPONSE = True
QUIT_COMMAND = "/quit"
G = 17
N = 127


def client_loop(client: socket):
    while True:
        message = input("> ")

        if message.lower() == QUIT_COMMAND:
            break

        r1 = diffie_hellman(G, N, random.randint(1, 1000000))


def execute_client_loop(client: socket, print_response: bool = False):
    while True:
        message = input("> ")

        message = encrypt_with_caesar_cypher(message)

        client.send(message)
        response = str(client.recv(1024), "utf-8")

        if print_response:
            print(f"> Server response: {response}")


def main():
    client = None
    try:
        client = connect_to_server(SERVER_ADDRESS, SERVER_PORT)
        execute_client_loop(client)
    finally:
        if client:
            client.close()


if __name__ == "__main__":
    main()
    print(encrypt_with_caesar_cypher("ABC", 10))
