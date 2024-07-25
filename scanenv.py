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

    def packet_callback(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            if src_ip not in active_hosts:
                active_hosts.add(src_ip)
            if dst_ip not in active_hosts:
                active_hosts.add(dst_ip)

        active_hosts = set()
        
        sniff(prn=packet_callback, store=0, timeout=30)

        print("ACTIVE NETWORK DEVICES:")
        for host in active_hosts:
            print(host)
