from multiprocessing import Process, Queue
import zmq
import sys
import time


def client(ip):
    context = zmq.Context()
    print "Connecting to server..."
    socket = context.socket(zmq.SUB)
    socket.connect(ip)
    socket.setsockopt(zmq.SUBSCRIBE, "")
    print "waiting"
    print "Sent: %s" %socket.recv(100)
    time.sleep(0.2)

def server():
    context = zmq.Context()
    print "Connecting to server..."
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:7315")
    while True:
        text = raw_input("Type something\n")
        socket.send(text)

for i in range(0, 255):
    ip = "tcp://192.168.43.%d:7315" %i
    p = Process(target=client, args=(ip,))
    p.start()
server()
