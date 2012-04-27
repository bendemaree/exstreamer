#!/usr/bin/python

from exstreamer.exstreamer import *

class TestVolume:
    def setup_method(self, method):
        self.ex = Exstreamer('192.168.10.101')
    
    def test_volume_set(self):
        self.ex.set_volume(15)
        assert self.ex.get_volume() == 15
        self.ex.set_volume(100)
        assert self.ex.get_volume() == 100
        self.ex.set_volume(30)
        assert self.ex.get_volume() == 30
        
    def test_volume_mute(self):
        assert self.ex.get_volume() != False

        self.ex.set_mute(True)
        assert self.ex.get_mute() == True
        assert self.ex.get_volume() == False

        self.ex.set_mute(False)
        assert self.ex.get_mute() == False
        assert self.ex.get_volume() != False

        self.ex.set_mute(True)
        self.ex.set_volume(45)
        assert self.ex.get_mute() == False
        assert self.ex.get_volume() == 45
