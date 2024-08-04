import sys
import os
import scanenv
from pyfiglet import Figlet

def banner(titel):
    f = Figlet(font='avatar')
    print(f.renderText(titel))

# contains any active recon scan option
class Hostdiscovery:

    def __init__(self, discover_command):
        self.discover_command = discover_command

    def ping_host(ip_address):
        scanenv.icmp_echo(ip_address)

    def arp_scan(ip_address_range):
        scanenv.arp_scan(ip_address_range)

    def icmp_host_discover(ip_address_range):
        scanenv.icmp_host_discover(ip_address_range)

# contains any control option of the user and its mechanisms
class AttackController:

    def __init__(self):
        pass

    def user_action(self, user_command):
        if user_command == "1":
            ip_destionation = input("[*] DESTINATION IP ADDRESS: ")
            scanenv.icmp_echo(ip_destionation)
        if user_command == "2":
            ip_address_range = input("[*] IP ADDRESS RANGE (f.e. 192.168.1.0/24): ")
            scanenv.arp_scan(ip_address_range)
        if user_command == "3":
            ip_address_range = input("[*] IP ADDRESS RANGE (f.e. 192.168.1.0/24): ")
            scanenv.icmp_host_discover(ip_address_range)
        if user_command == "4":
            ip_address_range = input("[*] IP ADDRESS RANGE (f.e. 192.168.1.0/24): ")
            scanenv.nmap_host_discover(ip_address_range)


def main():

    try:

        banner("PY$SPLOIT")
        print("[1]\tICMP ECHO REPLY (ping host)")
        print("[2]\tARP SCAN")
        print("[3]\tICMP HOST DISCOVER")
        print("[4]\tNMAP HOST DISCOVER")
        print("[99]\tEXIT\n")

        user_command = input("[$]> ")

        AttackController().user_action(user_command)


    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(f"[-] Error occured - {e}")
        sys.exit()

if __name__ == '__main__':

    os.system("clear")

    main()