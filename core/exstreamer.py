#!/usr/bin/python

import socket
from lxml import etree

from util import *

class Exstreamer:
    def __init__(self, ip, port=DEFAULT_COMMAND_PORT):
        self.ip = ip
        self.port = port
        self.connection = None

    def get_volume(self):
        if not self.is_connected():
            self.connect()

        self.connection.send(wrap_command(CMD_GETVOLUME))
        raw_vol = self.connection.recv(BUFFER_SIZE)
        vol_xml = etree.fromstring(raw_vol) # create xml representation
        return int(vol_xml.text) * 5  # convert to percentage

    def set_volume(self, vol):
        if not self.is_connected(): 
            connect()

        # volume levels are defined 0 thru 20 (off thru max)
        # we will accept a volume percentage
        if(vol > 100 or vol < 0):
            raise InvalidVolumeLevel('That volume is out of range.')
        vol = round_to_base(vol, 5) / 5  # convert to base 0 thru 20
        print vol
        self.connection.send(wrap_command(CMD_SETVOLUME, vol))
        self.connection.recv(BUFFER_SIZE)  # receive and discard ACK

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        self.connection = s

    def is_connected(self):
        if self.connection is None:
            return False
        else:
            return True
