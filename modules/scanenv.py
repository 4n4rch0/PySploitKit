import os
import sys
import subprocess
import nmap
from prettytable import PrettyTable
from ipaddress import IPv4Network

def icmp_echo(ip_destionation):
    response = os.popen("ping -c 4 " + ip_destionation).readlines()
    if response == 0:
        for output_line in response:
            print(output_line[1])
    else:
        print(f"[ERROR]\tNo ICMP ECHO reply by hopst {ip_destionation}.")
        pass

def arp_scan(ip_address_range):

    try:

        print("\n")

        response = os.popen(f"sudo arp-scan {ip_address_range}").readlines()
        response.remove(response[0])

        for output_line in response:

            if output_line.replace("\n","") == "":
                break

            arp_host = output_line.replace("\n","")
            print(f"[ARP SCAN]\t{arp_host}")

        print("\n")
            
    except Exception as e:

        print(f"[ERROR]\t{e}")
        sys.exit()

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