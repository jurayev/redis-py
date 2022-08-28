def respond_err(client_conn, addr):
    client_conn.sendall(b"-ERR unknown command\r\n")
    print(f"Send ERR reply to {addr}")