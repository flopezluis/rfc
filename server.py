import zmq
import time
import sys

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:7313")
message = socket.recv()
print "Received request: ", message
