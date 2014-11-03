import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind("tcp://*:7314")
socket.setsockopt(zmq.SUBSCRIBE, "")
print  socket.recv()
