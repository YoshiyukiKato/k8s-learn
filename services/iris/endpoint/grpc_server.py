from concurrent import futures
import time
import grpc
from protos import iris_pb2
from protos import iris_pb2_grpc
import numpy as np
from sklearn import datasets
from sklearn.externals import joblib

iris = datasets.load_iris()
model = joblib.load('model/clf.pkl') 

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Iris(iris_pb2_grpc.IrisServicer):
    def Predict(self, request, context):
        try:
            print(request.data)
            print(np.array([request.data]))
            label = model.predict(np.array([request.data]))
            print(label)
            return iris_pb2.IrisResponse(label=label)
        except Exception as e:
            # logging error
            print(e)
            # switch by error message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iris_pb2_grpc.add_IrisServicer_to_server(Iris(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()