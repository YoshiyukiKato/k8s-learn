
from __future__ import print_function

import grpc
from lib.grpc import user_state_pb2
from lib.grpc import user_state_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_state_pb2_grpc.UserStateStub(channel)
        response = stub.Get(user_state_pb2.GetRequest(id=1))
    print(response)


if __name__ == '__main__':
    run()