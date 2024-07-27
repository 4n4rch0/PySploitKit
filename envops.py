import subprocess

def icmp_reply(ip_address):

    ping_process = subprocess.Popen(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ping_output, ping_errors = ping_process.communicate()

    print("[ICMP ECHO REPLY]" f'{ping_output}')
    print("[ICMP RESPONSE]" f'{ping_errors}')

ip_dest = "8.8.8.8"

icmp_reply(ip_dest)