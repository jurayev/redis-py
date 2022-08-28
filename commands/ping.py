
def respond_ping(client_conn, addr):
    client_conn.sendall(b"+PONG\r\n")
    print(f"Send PONG reply to {addr}")
