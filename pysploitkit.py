import sys
import scanenv
from pyfiglet import Figlet

def banner(titel):
    f = Figlet(font='slant')
    print(f.renderText(titel))

class Coordination:
    pass

def main():

    try:

        banner("PY$SPLOIT")

        ip_address = input("[?] Enter an IP address: ")

        Discovery().icmp_request(ip_address)

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(f"[-] Error occired - {e}")
        sys.exit()

if __name__ == '__main__':

    main()