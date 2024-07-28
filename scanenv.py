import time
import os

def icmp_echo(ip_destionation):
    response = os.system("ping -c 4 " + ip_destionation)
    if response == 0:
        print("PING {}.".format(response))
    else:
        pass
