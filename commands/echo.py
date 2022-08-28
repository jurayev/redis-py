
def respond_echo(client_conn, addr, *data):
    strings = "".join(*data)
    client_conn.sendall(f"+{strings}\r\n".encode())
    print(f"Send ECHO reply to {addr}")
