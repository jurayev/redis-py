import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 6539  # The port used by the server


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("PING, Y/N?")
        while input().lower() == "y":
            s.sendall(f"+PING from {HOST}:{PORT}\r\n".encode())
            data = s.recv(1024)
            print(f"Received {data!r}")
            print("PING again, Y/N?")


if __name__ == "__main__":
    main()
