#!/usr/bin/python

import socket
import util

class Connection:
    def __init__(self, ip, port):
        self.connection = None
        self.ip = ip
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.settimeout(util.TIMEOUT)
        self.connection.connect((self.ip, self.port))

    def __del__(self):
        self.connection.close()
        self.connection = None

    def sendcmd(self, command, content=''):
        self.connection.send(util.wrapcmd(command, content))

    def recvcmd(self):
        return self.connection.recv(util.BUFFER_SIZE)

    def get_connection(self):
        return self.connection

    def get_ip(self):
        return self.ip

    def get_port(self):
        return port
