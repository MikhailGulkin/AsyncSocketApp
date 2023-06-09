import socket

from src.domain.consts.client_messages import EXIT
from src.domain.interfaces import BaseSocket
from src.infrastructure.adapters.io import BaseSocketIO


class BaseClient:
    def __init__(
            self,
            client: BaseSocket,
            socket_io: BaseSocketIO
    ):
        self.client = client
        self.client_io = socket_io

    async def _close_all_connection(self):
        self.client_io.delete_messages_file()
        self.client.socket.close()

    async def _send_information_on_server(self):
        if self.client_io.socket_input.value:
            self.client.socket.send(self.client_io.socket_input.value.encode())
            await self.client_io.socket_input.get_input()

    async def _send_last_exit_message(self):
        self.client.socket.send(EXIT.encode())

    async def _retrieve_information_from_server(self):
        try:
            request = self.client.socket.recv(self.client.config.RECV).decode()
        except socket.timeout:
            return
        if request:
            await self.client_io.socket_output.write_message(
                f'Message from server {request}'
            )
