#!/usr/bin/python

import util
import socket

class Connection:
    def __init__(self, ip, port):
        self.connection = None
        self.ip = ip
        self.port = port
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        self.connection = s

    def __del__(self):
        self.connection.close()
        self.connection = None

    def get_connection(self):
        return self.connection

    def get_ip(self):
        return self.ip

    def get_port(self):
        return port
