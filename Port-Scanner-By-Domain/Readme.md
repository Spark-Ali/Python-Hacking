# Port-Scanner_By-Domain

PortScanner is made in Python for Discovering Open UDP/TCP Ports by IP Address and Domain Name Both.

# Installation

*You have to run this command to install portscanner*

```
$ git clone https://github.com/Spark-Ali/Pythonhacking/Portscanner_By-Domain.git
```
*After installing Port_Scanner run this command to install requirement.txt*

```
$ pip3 install -r requirement.txt
```
# Usage

*Enter your target's IP ADDRESS or DOMAIN NAME in required input*

## For Example

```
[+] Input The Target Ip or Domain : www.google.com
```
# Port Range

*Enter your target's portrange in range() Enter the port number where you want to start scan and split it by , (Comma) And Enter port where you want to end Scan :*

```
for port in range(79,85):#Enter The Range Of Ports In Brackets (1,65535)
    port_scanner(converted_ip, port)
```
# Results
```
[+] Input The Target Ip or Domain : www.google.com
--------------------------------------------------
The Target is www.google.com
Scan Started On 2021-06-07 00:15:38.432937
--------------------------------------------------
[-] Port 79 is Closed
[+] Port 80 is Open 
[-] Port 81 is Closed
[-] Port 82 is Closed
[-] Port 83 is Closed
[-] Port 84 is Closed
```