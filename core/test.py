#!/usr/bin/python

from exstreamer import *

ex1 = Exstreamer('192.168.10.101')
print "Current volume: " + str(ex1.get_volume())
print "Changing volume..."
ex1.set_volume(65)
print "New volume: " + str(ex1.get_volume())
