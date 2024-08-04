import os
import nmap
from scapy.all import ARP, Ether, srp, IP, ICMP, sr1
from prettytable import PrettyTable
from ipaddress import IPv4Network

def icmp_echo(ip_destionation):
    response = os.system("ping -c 4 " + ip_destionation)
    if response == 0:
        print("PING {}.".format(response))
    else:
        pass

def arp_scan(ip_address_range):

    arp = ARP(pdst=ip_address_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    table = PrettyTable(["IP Address", "MAC Address"])
    for sent, received in result:
        table.add_row([received.psrc, received.hwsrc])

    print(table)

def icmp_host_discover(network_range):

    live_hosts = []

    for ip in IPv4Network(network_range).hosts():

        packet = IP(dst=str(ip))/ICMP()
        response = sr1(packet, timeout=2, verbose=0)

        if response:
            live_hosts.append((response[IP].src, response[ICMP].type))

    table = PrettyTable(["IP Address", "ICMP Type"])
    for host in live_hosts:
        table.add_row([host[0], host[1]])

    print(table)

def nmap_host_discover(network_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments='-sn')

    live_hosts = []
    for host in nm.all_hosts():
        live_hosts.append((host, nm[host]['status']['state']))

    table = PrettyTable(["IP Address", "Status"])
    for host in live_hosts:
        table.add_row([host[0], host[1]])

    print(table)