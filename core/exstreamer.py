#!/usr/bin/python

import socket
from lxml import etree

from util import *

class Exstreamer:
    def __init__(self, ip, port=DEFAULT_COMMAND_PORT):
        self.ip = ip
        self.port = port
        self.connection = None
        self.volume = None

        self.connect()
        self.set_mute(False)

    def get_device_volume(self):
        if not self.is_connected():
            self.connect()
        
        self.connection.send(wrap_command(CMD_GETVOLUME))
        raw_vol = self.connection.recv(BUFFER_SIZE)
        vol_xml = etree.fromstring(raw_vol) # create xml representation
        return int(vol_xml.text) * 5  # convert to percentage

    def get_volume(self):
        if not self.is_connected():
            self.connect()
        
        return self.volume

    def set_volume(self, vol):
        if not self.is_connected():
            self.connect()

        # volume levels are defined 0 thru 20 (off thru max)
        # we will accept a volume percentage
        if(vol > 100 or vol < 0):
            raise InvalidVolumeLevel('That volume is out of range.')
        converted_vol = round_to_base(vol, 5) / 5  # convert to base 0 thru 20
        self.connection.send(wrap_command(CMD_SETVOLUME, converted_vol))
        self.connection.recv(BUFFER_SIZE)  # receive and discard ACK
        self.volume = vol

    def get_mute(self):
        if not self.is_connected():
            self.connect()
        
        if not self.get_volume():
            return True
        return False

    def set_mute(self, state):
        if not self.is_connected():
            self.connect()

        if state:
            self.connection.send(wrap_command(CMD_MUTEON))
            self.connection.recv(BUFFER_SIZE)
            self.volume = False
        else:
            self.connection.send(wrap_command(CMD_MUTEOFF))
            self.connection.recv(BUFFER_SIZE)
            self.volume = self.get_device_volume()

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        self.connection = s

    def disconnect(self):
        if(self.connection == None):
            return True

        self.connection.close()
        self.connection = None

        # make stored values stale
        self.volume = None

    def is_connected(self):
        if self.connection is None:
            return False
        else:
            return True
