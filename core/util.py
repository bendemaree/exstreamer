 #!/usr/bin/python

DEFAULT_COMMAND_PORT = 12302
BUFFER_SIZE = 1024

CMD_GETVOLUME = 'L=volume.ack'
CMD_SETVOLUME = 'v='
CMD_TERMINATOR = '\n'

def round_to_base(x, base=5):
    return int(base * round(float(x)/base))

def wrap_command(command, content=''):
    return command + str(content) + CMD_TERMINATOR
