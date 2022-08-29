import random
import socket
import sys

from env.env import environment as env


def handle_ping(s):
    print("PING, Y/N?")
    while input().lower() == "y":
        s.sendall(f"*1\r\n$4\r\nPING\r\n".encode())
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

def handle_set(s):
    print("SET, Y/N?")
    keys = ["hey", "banana", "hello", "world"]
    values = ["1", "banana", "water", "apple", "tennis"]
    while input().lower() == "y":
        key, value = random.choice(keys), random.choice(values)
        s.sendall(f"*3\r\n$3\r\nSET\r\n${len(key)}\r\n{key}\r\n${len(value)}\r\n{value}\r\n".encode())
        data = s.recv(1024)
        print(f"Received {data}")
        print("SET again, Y/N?")


def handle_get(s):
    print("GET, Y/N?")
    values = ["hey", "banana", "hello", "world", "tennis"]
    while input().lower() == "y":
        value = random.choice(values)
        s.sendall(f"*2\r\n$4\r\nGET\r\n${len(value)}\r\n{value}\r\n".encode())
        data = s.recv(1024)
        print(f"Received {data}")
        print("GET again, Y/N?")


def main(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((env.get("HOST"), env.get("PORT")))

        if command == "PING":
            handle_ping(s)
        elif command == "ECHO":
            handle_echo(s)
        elif command == "SET":
            handle_set(s)
        elif command == "GET":
            handle_get(s)
        else:
            raise Exception(f"Unsupported command type {sys.argv[1]}")

    print("Disconnected")


if __name__ == "__main__":
    command = sys.argv[1].upper()
    main(command)
