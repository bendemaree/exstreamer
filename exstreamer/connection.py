#!/usr/bin/python

import socket

class Connection:
    def __init__(self, ip, port):
        self.connection = None
        self.ip = ip
        self.port = port
        print "2"        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "2.5"
        s.connect((self.ip, self.port))
        self.connection = s
        print "3"
    def __del__(self):
        self.connection.close()
        self.connection = None
        print "4"
    def get_connection(self):
        return self.connection

    def get_ip(self):
        return self.ip

    def get_port(self):
        return port
