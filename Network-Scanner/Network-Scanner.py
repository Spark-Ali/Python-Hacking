import nmap
from scapy import main
from datetime import datetime


class Network(object):
    def __init__(self, ip= " "):
        ip = input("[+] Enter Your Router's Ip address : ")
        self.ip = ip




    def NetworkScannner(self):
        if len(self.ip) == 0:
            network = "192.168.100.1/24"
        else:
            network = self.ip + '/24'
        print('-' * 50)
        print(f'Scan Started at {str(datetime.now())}')
        print('-' * 50)

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        host_list = [(x, nm[x] ['status'] ['state']) for x in nm.all_hosts()]
        for host, status in host_list:
            print(f'Host\t{host} is Online ')
if __name__ == "__main__":
    D = Network()
    D.NetworkScannner()



