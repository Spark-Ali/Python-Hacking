import socket
from datetime import datetime
from IPy import IP


ip_address = input("[+] Input The Target Ip or Domain : ")#Enter Ip Address Of Target You Can Also Input Domain Name

# def check_ip will help to scan by Domain Name Or Ip Address
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def port_scanner(ip_address, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip_address, port))
        print(f"[+] Port {str(port)} is Open ")
    except:
        print(f"[-] Port {str(port)} is Closed")



print('-' * 50)
print(f"The Target is {ip_address}")
print(f"Scan Started On {str(datetime.now())}")
print('-' * 50)

converted_ip = check_ip(ip_address)

for port in range(79,85):#Enter The Range Of Ports In Brackets (1,65535)
    port_scanner(converted_ip, port)

