import sys
import subprocess
from pyfiglet import Figlet

def banner(titel):
    f = Figlet(font='slant')
    print(f.renderText(titel))

class WebRequest:

    def __init__(self) -> None:
        pass

    def icmp_reply(self, ip_address):

        ping_process = subprocess.Popen(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_output, ping_errors = ping_process.communicate()

        print("[ICMP ECHO REPLY]", ping_output.decode('utf-8'))
        print("[ICMP RESPONSE]", ping_errors.decode('utf-8'))


class Discovery:

    def __init__(self):
        pass

def main():

    try:

        banner("PY$SPLOIT")

        dest_ip = "1.1.1.1"     # Cloudflare zwecks testen

        WebRequest().icmp_reply(dest_ip)

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(f"[-] Error occired - {e}")
        sys.exit()

if __name__ == '__main__':

    main()