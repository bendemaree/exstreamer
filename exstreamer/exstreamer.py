#!/usr/bin/python

import util
import connection
from lxml import etree

class Exstreamer:
    def __init__(self, ip, port=util.DEFAULT_COMMAND_PORT):
        self.volume = None
        self.shuffle = None
        self.loudness = None
        self.state = None
        
        self.heldconnection = connection.Connection(ip, port)
        self.connection = self.heldconnection
        self.set_mute(False)
        self.set_shuffle(False)
        self.set_loudness(False)
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
        self.state = util.STATE_STOP

    def pause(self):
        # Force this to toggle.
        if self.state == util.STATE_PAUSE:
            self.connection.sendcmd(util.CMD_PAUSE)
            self.connection.recvcmd()
            self.state = util.STATE_PLAY
        elif self.state == util.STATE_PLAY:
            self.connection.sendcmd(util.CMD_PAUSE)
            self.connection.recvcmd()
            self.state = util.STATE_PAUSE

    def next(self):
        # The Exstreamers have built-in rules as to what happens if you hit next and
        # there is no playlist running (inevitably something will start playing). We
        # are going to override that to stay more in control. It's not a terribly
        # common scenario, anyway.
        if self.state == util.STATE_PLAY:
            self.connection.sendcmd(util.CMD_NEXT)
            self.connection.recvcmd()

    def previous(self):
        # See comment of next()
        if self.state == util.STATE_PLAY:
            self.connection.sendcmd(util.CMD_PREVIOUS)
            self.connection.recvcmd()

    def get_status(self):
        if self.state == util.STATE_PLAY:
            return "Playing"
        elif self.state == util.STATE_PAUSE:
            return "Paused"
        elif self.state == util.STATE_STOP:
            return "Stopped"

    def set_shuffle(self, shuffle):
        if shuffle == True:
            self.connection.sendcmd(util.CMD_SHUFFLEON)
            self.connection.recvcmd()
            self.shuffle = True
        elif shuffle == False:
            self.connection.sendcmd(util.CMD_SHUFFLEOFF)
            self.connection.recvcmd()
            self.shuffle = False

    def get_shuffle(self):
        return self.shuffle

    def set_loudness(self, loudness):
        if loudness == True:
            self.connection.sendcmd(util.CMD_LOUDNESSON)
            self.connection.recvcmd()
            self.loudness = True
        elif loudness == False:
            self.connection.sendcmd(util.CMD_LOUDNESSOFF)
            self.connection.recvcmd()
            self.loudness = False

    def get_loudness(self):
        return self.loudness

    def set_source(self, source):
        if source == util.SRC_SERIAL:
            self.connection.sendcmd(util.CMD_SRCSERIAL)
            self.connection.recvcmd()
            self.source = util.SRC_SERIAL
        elif source == util.SRC_LINEIN:
            self.connection.sendcmd(util.CMD_SRCLINEIN)
            self.connection.recvcmd()
            self.source = util.SRC_LINEIN
        elif source == util.SRC_MICIN:
            self.connection.sendcmd(util.CMD_SRCMICIN)
            self.connection.recvcmd()
            self.source = util.SRC_MICIN
        else:
            raise InvalidSource('That is not a valid play source.')

    def get_source(self):
        if source == util.SRC_SERIAL:
            return 'Serial'
        elif source == util.SRC_LINEIN:
            return 'Line In'
        elif source == util.SRC_MICIN:
            return 'Mic In'

    def reboot(self):
        self.connection.sendcmd(util.CMD_REBOOT)
