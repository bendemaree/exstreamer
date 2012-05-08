 #!/usr/bin/python

import time

DEFAULT_COMMAND_PORT = 12302
BUFFER_SIZE = 4096
TIMEOUT = 10 # seconds
CMD_TERMINATOR = '\n'

CMD_GETVOLUME = 'L=volume.ack'
CMD_SETVOLUME = 'v='
CMD_MUTEON = 'c=40'
CMD_MUTEOFF = 'c=41'
CMD_STOP = 'c=2'
CMD_PAUSE = 'c=3'
CMD_NEXT = 'c=4'
CMD_PREVIOUS = 'c=5'
CMD_GETCONFIG = 'L=getconfig.ack'
CMD_SHUFFLEON = 'c=6'
CMD_SHUFFLEOFF = 'c=7'
CMD_LOUDNESSON = 'c=9'
CMD_LOUDNESSOFF = 'c=10'
CMD_SRCSERIAL = 'c=27'
CMD_SRCLINEIN = 'c=28'
CMD_SRCMICIN = 'c=29'
CMD_REBOOT = 'c=99'

CFG_STARTCFG = 'C='
CFG_CFGPREFIX = 'L='
CFG_IP = ['B0', 'B1', 'B2', 'B3']
CFG_GATEWAYIP = ['B4', 'B5', 'B6', 'B7']
CFG_SUBNETMASK = ['N8B0', 'N8B1', 'N8B2', 'N8B3']
CFG_WLANMODE = 'B9'
CFG_WLANSSID = 'S10'
CFG_WEPMODE = 'W43'
CFG_WEPKEY = 'S45'
CFG_DNSPRIMARY = ['B64', 'B65', 'B66', 'B67']
CFG_DNSSECONDARY = ['B68', 'B69', 'B70', 'B71']

SRC_SERIAL = 1000
SRC_LINEIN = 1001
SRC_MICIN = 1002

STATE_PLAY = 1003
STATE_PAUSE = 1004
STATE_STOP = 1005

def round_to_base(x, base=5):
    return int(base * round(float(x)/base))

def wrapcmd(command, content=''):
    return command + str(content) + CMD_TERMINATOR

def format_settings(command, settings=[]):
    command = CFG_STARTCFG
    print settings
    for setting in settings:
        print setting
        wrap_setting = CFG_CFGPREFIX + setting
        command += (CFG_CFGPREFIX + wrap_setting + CMD_TERMINATOR)
    return command + CMD_TERMINATOR
