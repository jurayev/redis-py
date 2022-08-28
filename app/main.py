import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    sock, addr = server_socket.accept()
    response = sock.recv(1024)
    sock.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
