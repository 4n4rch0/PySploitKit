from scapy import *
import scapy.all as scapy
import subprocess
import sys, os

class RequestHost:

    def __init__(self):
        pass

    def icmp_echo(self, ip_address):

        ping_process = subprocess.Popen(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_output, ping_errors = ping_process.communicate()

        print(ping_output.decode())

    def directory_fuzz(self, fuzzing_list):
        pass