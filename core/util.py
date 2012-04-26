 #!/usr/bin/python

import time

DEFAULT_COMMAND_PORT = 12302
BUFFER_SIZE = 1024

CMD_GETVOLUME = 'L=volume.ack'
CMD_SETVOLUME = 'v='
CMD_MUTEON = 'c=40'
CMD_MUTEOFF = 'c=41'
CMD_GETCONFIG = 'L=getconfig.ack'

CMD_TERMINATOR = '\n'

def recvall(con, timeout=2):
    con.setblocking(0)
    total_data=[];
    data='';
    begin=time.time()
    while 1:
        if total_data and time.time()-begin>timeout:
            break
        elif time.time()-begin>timeout*2:
            break
        try:
            data = con.recv(BUFFER_SIZE)
            if data:
                total_data.append(data)
                begin=time.time()
            else:
                time.sleep(0.1)
        except:
            pass
    return ''.join(total_data)

def round_to_base(x, base=5):
    return int(base * round(float(x)/base))

def wrap_command(command, content=''):
    return command + str(content) + CMD_TERMINATOR
