import scapy.all as scapy
import socket

def banner():
    pass

class Scanner:

    def __init__(self, target_data):
        self.target_data = target_data

    def get_device(self):
        pass

    def get_network_devices(self):
        pass

class Modules:

    def __init__(self, listener_ip, listener_port):
        self.listener_ip = listener_ip
        self.listener_port = listener_port

    def start_listener(self):
        pass

    def send_generic_payload(self):
        pass

    def send_ssh_payload(self):
        pass

    def send_windows_payload(self):
        pass

    def send_linux_payload(self):
        pass

    def send_android_payload(self):
        pass

class Commander:

    def __init__(self, command_instructionn):
        self.command_instructionn = command_instructionn


def main():

    pass

if __name__ == '__main__':

    main()