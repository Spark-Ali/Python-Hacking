import sys
import socket
from datetime import datetime



#Target Defination
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid Amount of Arguments')
    print('Syntax : Python3 Port-scanner.py <ip>')

print('-' * 50)
print(f"Scanning Target {target}")
print(f"Scan Started On {str(datetime.now())}")
print('-' * 50)


try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        # print(f'Scanning Port {format(port)}')
        if result == 0:
            print(f'Port {format(port)} is Open ')
            s.close
        
except KeyboardInterrupt:
    print('\n Exiting Program')
    print(f"Scan Ended On {str(datetime.now())}")
    sys.exit()
except socket.gaierror:
    print('HostName Could Not Be Resolved :(')
    print(f"Scan Ended On {str(datetime.now())}")
    sys.exit()
except socket.error:
    print('Could not Connect To The Server')
    print(f"Scan Ended On {str(datetime.now())}")
    sys.exit()