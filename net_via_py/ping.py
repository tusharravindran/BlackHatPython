import socket
import sys

try:
#AF_NET refers to address family ipv4 and SOCK_STREAM means communication in TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("ERROR in socket creation with error %s"%(err))
finally:
       print("*"*100)
port=80
try:
    host_ip = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Cannot resolve host")
except IndexError:
    print("Syntax error")
    print("Syntax: python3 test.py ip")
    print("python3 test.py 127.0.0.1")
    sys.exit()
s.connect((host_ip, port))
print("port connected on port number == %s and ip == %s " %(port, host_ip ))