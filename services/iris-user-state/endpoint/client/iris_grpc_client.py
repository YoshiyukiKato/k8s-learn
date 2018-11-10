"""gRPC client"""
from __future__ import print_function
import grpc
from lib.grpc import iris_state_pb2, iris_state_pb2_grpc

def get(stub, iris_id):
    """get"""
    return stub.Get(
        iris_state_pb2.GetRequest(
            iris_id=iris_id))


def update(stub, iris_id, params):
    """update"""
    return stub.Update(
        iris_state_pb2.UpdateRequest(
            iris_id=iris_id,
            params=params))

def batch_update(stub, iris_id, params_list):
    """batch update"""
    return stub.BatchUpdate(
        iris_state_pb2.BatchUpdateRequest(
            iris_id=iris_id,
            paramsList=params_list))

def run():
    """run"""
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = iris_state_pb2_grpc.IrisStateStub(channel)
        print(get(stub, "1"))

if __name__ == '__main__':
    run()