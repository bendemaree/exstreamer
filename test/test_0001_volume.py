#!/usr/bin/python

from exstreamer.exstreamer import *

def test_volume():
    # Setting
    ex = Exstreamer('192.168.10.100')
    ex.set_volume(15)
    assert ex.get_volume() == 15
    ex.set_volume(100)
    assert ex.get_volume() == 100
    ex.set_volume(30)
    assert ex.get_volume() == 30
    
    # Muting
    assert ex.get_volume() != False

    ex.set_mute(True)
    assert ex.get_mute() == True
    assert ex.get_volume() == False

    ex.set_mute(False)
    assert ex.get_mute() == False
    assert ex.get_volume() != False

    ex.set_mute(True)
    ex.set_volume(45)
    assert ex.get_mute() == False
    assert ex.get_volume() == 45

    # Shuffle
    assert ex.get_shuffle() == False

    ex.set_shuffle(True)
    assert ex.get_shuffle() == True
    ex.set_shuffle(False)
    assert ex.get_shuffle() == False

    # Loudness
    assert ex.get_loudness() == False

    ex.set_loudness(True)
    assert ex.get_loudness() == True
    ex.set_loudness(False)
    assert ex.get_loudness() == False
