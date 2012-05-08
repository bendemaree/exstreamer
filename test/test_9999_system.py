#!/usr/bin/python

from exstreamer.exstreamer import *

def test_system():
    # Setting
    ex = Exstreamer('192.168.10.100')

    ex.reboot()
    try:
        ex.get_volume()
    except:
        pass
