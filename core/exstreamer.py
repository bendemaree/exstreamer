#!/usr/bin/python

import connection
from lxml import etree
from util import *

class Exstreamer:
    def __init__(self, ip, port=DEFAULT_COMMAND_PORT):
        self.volume = None
        
        self.heldconnection = connection.Connection(ip, port)
        self.connection = self.heldconnection.get_connection()

        self.set_mute(False)

    def get_device_volume(self):
        self.connection.send(wrap_command(CMD_GETVOLUME))
        raw_vol = self.connection.recv(BUFFER_SIZE)
        vol_xml = etree.fromstring(raw_vol) # create xml representation
        return int(vol_xml.text) * 5  # convert to percentage

    def get_volume(self):
        return self.volume

    def set_volume(self, vol):
        # volume levels are defined 0 thru 20 (off thru max)
        # we will accept a volume percentage
        if(vol > 100 or vol < 0):
            raise InvalidVolumeLevel('That volume is out of range.')
        converted_vol = round_to_base(vol, 5) / 5  # convert to base 0 thru 20
        self.connection.send(wrap_command(CMD_SETVOLUME, converted_vol))
        self.connection.recv(BUFFER_SIZE)  # receive and discard ACK
        self.volume = vol

    def get_mute(self):
        if not self.get_volume():
            return True
        return False

    def set_mute(self, state):
        if state:
            self.connection.send(wrap_command(CMD_MUTEON))
            self.connection.recv(BUFFER_SIZE)
            self.volume = False
        else:
            self.connection.send(wrap_command(CMD_MUTEOFF))
            self.connection.recv(BUFFER_SIZE)
            self.volume = self.get_device_volume()

