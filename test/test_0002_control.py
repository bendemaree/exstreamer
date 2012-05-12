from exstreamer.exstreamer import *

def test_control():
    ex = Exstreamer('192.168.10.100')
    cn = Configuration(ex)
    cn.set_ip('192.168.10.101')
