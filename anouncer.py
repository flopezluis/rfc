import socket
import zmq
import sys
import time

def get_ip():
    return socket.gethostbyname(socket.gethostname())

context = zmq.Context()
print "Connecting to server..."
socket_pub = context.socket(zmq.PUB)
for i in range(0, 255):
    socket_pub.connect("tcp://192.168.43.%d:7314" %i)
    socket_pub.send(get_ip())
    time.sleep(0.1)
    print "sending to %d" %i
