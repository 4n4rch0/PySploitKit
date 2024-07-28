import time
import os

class RequestHost:

    def __init__(self):
        pass

def icmp_echo(ip_destionation):
    response = os.system("ping -c 4 " + ip_destionation)
    if response == 0:
        print("PING {}.".format(response))
        time.sleep()
    else:
        pass
