# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(10)
print ("socket is listen")

# a forever loop until we interrupt it or
# an error occurs
while True:

# Establish connection with client.
    c, addr = s.accept()
    c.send(b'Thank you for connecting')

#output = 'Thank you for connecting'
#c.sendall(output.encode('utf-8'))
# send a thank you message to the client.
# Close the connection with the client
    c.close()
    print("press ctrl + C to exit")