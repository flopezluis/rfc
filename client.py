import zmq
import sys

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:7313")
socket.connect ("tcp://localhost:7313")
socket.send ("Hello")
message = socket.recv()
print "Received reply %s" %message
