import scapy.all as scapy

def arp_scanner():
    print("[START ARP SCAN IN LOCAL AREA]")
    request = scapy.ARP()
    
    request.pdst = '192.168.0.1/24'
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
    request_broadcast = broadcast / request  
    clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0]  
    for element in clients:  
        print(str(element[1].psrc) + "      " + element[1].hwsrc)

def main():

    arp_scanner()

if __name__ == '__main__':

    main()