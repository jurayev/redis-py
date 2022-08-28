
def respond_ping(client_conn):
    client_conn.sendall(b"+PONG\r\n")
    print(f"Send PONG reply")
