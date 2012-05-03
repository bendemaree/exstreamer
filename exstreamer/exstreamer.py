#!/usr/bin/python

import util
import connection
from lxml import etree

class Exstreamer:
    def __init__(self, ip, port=util.DEFAULT_COMMAND_PORT):
        self.volume = None
        self.state = None
        
        self.heldconnection = connection.Connection(ip, port)
        self.connection = self.heldconnection
        self.set_mute(False)
        self.stop()

    def get_device_volume(self):
        self.connection.sendcmd(util.CMD_GETVOLUME)
        raw_vol = self.connection.recvcmd()
        vol_xml = etree.fromstring(raw_vol) # create xml representation
        return int(vol_xml.text) * 5  # convert to percentage

    def get_volume(self):
        return self.volume

    def set_volume(self, vol):
        # Volume levels are defined 0 thru 20 (off thru max).
        # We will accept a volume percentage (0% thru 100%).
        if(vol > 100 or vol < 0):
            raise InvalidVolumeLevel('That volume is out of range.')
        converted_vol = util.round_to_base(vol, 5) / 5  # convert to base 0 thru 20
        self.connection.sendcmd(util.CMD_SETVOLUME, converted_vol)
        self.connection.recvcmd()
        self.volume = vol

    def get_mute(self):
        if not self.get_volume():
            return True
        return False

    def set_mute(self, mute_state):
        if mute_state:
            self.connection.sendcmd(util.CMD_MUTEON)
            self.connection.recvcmd()
            self.volume = False
        else:
            self.connection.sendcmd(util.CMD_MUTEOFF)
            self.connection.recvcmd()
            self.volume = self.get_device_volume()

    def stop(self):
        # We can stop at any time; this command will always execute.
        self.connection.sendcmd(util.CMD_STOP)
        self.connection.recvcmd()
        self.state = "stop"

    def pause(self):
        # Force this to toggle.
        if self.state == "pause":
            self.connection.sendcmd(util.CMD_PAUSE)
            self.connection.recvcmd()
            self.state = "play"
        elif self.state == "play":
            self.connection.sendcmd(util.CMD_PAUSE)
            self.connection.recvcmd()
            self.state = "pause"

    def next(self):
        # The Exstreamers have built-in rules as to what happens if you hit next and
        # there is no playlist running (inevitably something will start playing). We
        # are going to override that to stay more in control. It's not a terribly
        # common scenario, anyway.
        if self.state == "play":
            self.connection.sendcmd(util.CMD_NEXT)
            self.connection.recvcmd()

    def previous(self):
        # See comment of next()
        if self.state == "play":
            self.connection.sendcmd(util.CMD_PREVIOUS)
            self.connection.recvcmd()

    def get_status(self):
        if self.state == "play":
            return "Playing"
        elif self.state == "pause":
            return "Paused"
        elif self.state == "stop":
            return "Stopped"
