import socket
import concurrent.futures
from commands.ping import respond_ping

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 6379  # The port used by the server


def handle_connection(client_conn, addr):
    with client_conn:
        print("--------------------------------")
        print(f"Connected to a client by {addr}")
        while True:
            data = client_conn.recv(1024)
            if not data:
                break
            print(f"Received the data from {addr} \n {data.decode()}")
            respond_ping(client_conn, addr)
            print("--------------------------------")

def main():
    # creates socket, bind to a port, start listening, returns socket obj
    server_socket = socket.create_server((HOST, PORT), reuse_port=True)
    print(f"Redis server is started and listening to {PORT}")
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            while True:
                client_conn, addr = server_socket.accept()  # wait for client accepting the connection
                executor.submit(handle_connection, client_conn, addr)
    except KeyboardInterrupt:
        pass
    print(f"Connection {addr} is closed")

    server_socket.close()
    print(f"Redis server was shutdown")


if __name__ == "__main__":
    main()
