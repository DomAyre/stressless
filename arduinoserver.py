import socket

class ArduinoServer:
    def __init__(self):
        # Setup the socket
        sock = socket.socket()
        sock.bind(("localhost", 8080))
        sock.listen(1)
        self.connection, client_address = sock.accept()

    def stream(self):                
        while True:
            self.connection.sendall("data")
        