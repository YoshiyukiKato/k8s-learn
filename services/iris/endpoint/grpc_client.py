
from __future__ import print_function

import grpc

from protos import iris_pb2
from protos import iris_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50001') as channel:
        stub = iris_pb2_grpc.IrisStub(channel)
        response = stub.Predict(iris_pb2.IrisRequest(data=[5.1,3.5,1.4,0.2]))
    print(response.label)


if __name__ == '__main__':
    run()