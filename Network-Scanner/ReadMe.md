# Python Network Scanner

_**Python Network Scanner for scanning online hosts on your network**_

# Installation

_**To install modules of this Script run this command**_

```
$ pip3 install -r requirement.txt
```
# Usage

*Enter your IP Address here to scan online hosts*
```
[+] Enter Your Router's Ip address : <Your-IPAddress>
```
# Customization

*If you don't want to enter your IP again and again then  Change the code as shown below*

```
 def NetworkScannner(self):
        if len(self.ip) == 0:
            network = "YOUR-IP/24"
        else:
            network = self.ip + '/YOUR-SUBNET'
```
_**After changing the code  just hit enter your scan will be started**_

# Results

```
-------------------------------------------
Scan Started at 2021-06-10 01:54:09.068701
-------------------------------------------
Host    192.168.100.1 is Online 
Host    192.168.100.10 is Online 
Host    192.168.100.2 is Online 
Host    192.168.100.4 is Online 
Host    192.168.100.9 is Online 
```