import socket

class Server:
    HEADER_LENGTH = 10

    SOCKETS_LIST= {}

def __init__(self, ip_address, port, af, type, protocol):
    self.ip_address = ip_address
    self.port = port
    self.af= af
    self.type = type
    self.protocol = protocol
    self.clients = list()
    
    """
    Creates the server anfd provides the address family and type of connection
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    """
    Sets the sokcet options where the first parameter is the level argument that manipulates thed other arguments.
    second option is to allow hte reuse of hte socket in case of a restart by the server, so if upon restart, 
    it doesn't throw  port in use erro
    """
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    #Binds the socket with the passed in ip and port number
    server_socket.bind((self.ip_address, self.port))
    server_socket.listen()

    global SOCKETS_LIST
    SOCKETS_LIST[self.port] = server_socket
    print(f'Listening for connections on IP = {self.ip_address} @ port = {self.port}')
    pass