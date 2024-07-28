import sys
import subprocess
from pyfiglet import Figlet

def banner(titel):
    f = Figlet(font='slant')
    print(f.renderText(titel))

class Coordination:
    pass

def main():

    try:

        banner("PY$SPLOIT")

        dest_ip = "1.1.1.1"     # Cloudflare zwecks testen

        WebRequest().icmp_reply(dest_ip)

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(f"[-] Error occured - {e}")
        sys.exit()

if __name__ == '__main__':

    main()