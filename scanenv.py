import time
import os
from scapy.all import ARP, Ether, srp
from prettytable import PrettyTable

def icmp_echo(ip_destionation):
    response = os.system("ping -c 4 " + ip_destionation)
    if response == 0:
        print("PING {}.".format(response))
    else:
        pass

def arp_scan(ip_address):
    arp = ARP(pdst=ip_address)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    table = PrettyTable(["IP Address", "MAC Address"])
    for sent, received in result:
        table.add_row([received.psrc, received.hwsrc])

    print(table)