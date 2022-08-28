import random
import socket
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 6379  # The port used by the server

def handle_ping(s):
    print("PING, Y/N?")
    while input().lower() == "y":
        s.sendall(f"+PING from {HOST}:{PORT}\r\n".encode())
        data = s.recv(1024)
        print(f"Received {data!r}")
        print("PING again, Y/N?")


def handle_echo(s):
    print("ECHO, Y/N?")
    strings = ["hey", "banana", "hello", "world"]
    while input().lower() == "y":
        s.sendall(f"*2\r\n$4\r\nECHO\r\n$3\r\n{random.choice(strings)}\r\n".encode())
        data = s.recv(1024)
        print(f"Received {data}")
        print("ECHO again, Y/N?")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        if sys.argv[1].upper() == "PING":
            handle_ping(s)
        elif sys.argv[1].upper() == "ECHO":
            handle_echo(s)
        else:
            raise Exception(f"Unsupported command type {sys.argv[1]}")

    print("Disconnected")


if __name__ == "__main__":
    main()
