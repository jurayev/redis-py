import socket
import concurrent.futures

from commands.commands import Commands
from storage.base_storage import BaseStorage
from utils.parser import RespParser


class Redis(Commands):
    def __init__(self, storage: BaseStorage, host: str, port: int, reuse: bool = True, workers: int = None):
        self.host = host
        self.port = port
        self.reuse = reuse
        self.workers = workers
        self.socket = None
        self.storage = storage

    def __enter__(self):
        self.socket = socket.create_server((self.host, self.port), reuse_port=self.reuse)
        print(f"Redis server is started and listening to {self.port}")
        return self

    def __exit__(self, *args, **kwargs):
        self.socket.close()
        print(f"Redis server was shutdown")

    def run(self):
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
                while True:
                    client_conn, addr = self.socket.accept()
                    executor.submit(self.handle_connection, client_conn, addr)
        except (KeyboardInterrupt, ConnectionError):
            pass

    def handle_connection(self, client_conn, addr):
        with client_conn:
            print("--------------------------------")
            print(f"Connected to a client by {addr}")
            while True:
                data = client_conn.recv(1024)
                if not data:
                    break
                data = data.decode()
                print(f"Received the data from {addr} \n {data}")
                strings = RespParser.parse_array(data)
                values = strings[1:]
                command = strings[0].upper() if strings else ""
                if command == "ECHO":
                    self.echo(client_conn, addr, values)
                elif command == "PING":
                    self.ping(client_conn, addr, values)
                elif command == "SET":
                    self.set(self.storage, client_conn, addr, values)
                elif command == "GET":
                    self.get(self.storage, client_conn, addr, values)
                else:
                    self.error(client_conn, addr, f"unknown command {command}", data)
                print("--------------------------------")
        print(f"Connection {addr} is closed")
