#!/usr/bin/python

import util
import connection
from lxml import etree
from exstreamer import *

class Configuration:
    def __init__(self, exstreamer):
        self.exstreamer = exstreamer
    
    def set_ip(self, ip):
        print util.format_settings(ip.split('.'))
        # self.exstreamer.connection.send(util.format_settings(ip.split('.')))
