class Commands:

    @staticmethod
    def set(storage, client_conn, addr, *data):
        try:
            key, value = data[0]
            storage.set(key, value)
            client_conn.sendall(b"+OK\r\n")
            print(f"Send SET OK to {addr}")
        except Exception:  # noqa
            Commands.error(client_conn, addr, "SET did not succeed", data)

    @staticmethod
    def get(storage, client_conn, addr, *data):
        try:
            key = data[0][0]
            value = storage.get(key)
            client_conn.sendall(f"+{value}\r\n".encode())
            print(f"Send GET {value} to {addr}")
        except (KeyError, Exception) as err: # noqa
            msg = f"{err}: GET did not succeed"
            Commands.error(client_conn, addr, msg, data)

    @staticmethod
    def error(client_conn, addr, message, *data):
        client_conn.sendall(f"-ERR {message} with data {data}\r\n".encode())
        print(f"Send ERR reply to {addr}")

    @staticmethod
    def echo(client_conn, addr, *data):
        strings = "".join(*data)
        client_conn.sendall(f"+{strings}\r\n".encode())
        print(f"Send ECHO reply to {addr}")

    @staticmethod
    def ping(client_conn, addr, *data):
        client_conn.sendall(b"+PONG\r\n")
        print(f"Send PONG reply to {addr}")