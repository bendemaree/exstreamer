#!/usr/bin/python

from exstreamer import *
import time

ex1 = Exstreamer('192.168.10.101')
print "Current volume: " + str(ex1.get_volume())
print "Changing volume..."
ex1.set_volume(65)
print "New volume: " + str(ex1.get_volume())
print "Mute status: " + str(ex1.get_mute())
print "Setting mute..."
time.sleep(1)
ex1.set_mute(True)
print "Mute status: " + str(ex1.get_mute())
