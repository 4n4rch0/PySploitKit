import os
import sys
import nmap
from prettytable import PrettyTable

def icmp_echo(ip_destionation):
    response = os.popen("ping -c 4 " + ip_destionation).readlines()
    if response != "":
        for x in range(0, len(response)-1):
            print(response[x])
    else:
        print(f"[ERROR]\tNo ICMP ECHO reply by hopst {ip_destionation}.")
        pass

def arp_scan(ip_address_range):

    try:

        print("\n")

        response = os.popen(f"sudo arp-scan {ip_address_range}").readlines()

        table = PrettyTable(["ARP LIVE HOSTS", "MAC ADDRESS", "DEVICE DATA"])
        print(table)

        for x in range(0, len(response)-1):
            arp_live_host = str(response[1+x].split(" ")[0])
            print(arp_live_host)
            # table.add_row(arp_live_host)

            if response[1+x].split(" ")[0].replace("\n","") == "":
                break

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