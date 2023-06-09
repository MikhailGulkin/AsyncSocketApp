import os
from pathlib import Path


class Config:
    class Paths:
        BASE_DIR = Path(__file__).absolute().parent.parent
        MESSAGES_DIR = BASE_DIR / os.path.join('presentation', 'messages')

    class Socket:
        SOCKET_TIMEOUT = 0.1
        SERVER_HOST = 'localhost'
        SERVER_PORT = 8000
        SERVER_LISTEN = 5
        RECV = 1024
