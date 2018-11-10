from concurrent import futures
import time
import grpc
import sys
from protos import iris_user_state_pb2, iris_user_state_pb2_grpc
from state import iris_state_service, user_state_service

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

iris = iris_state_service.IrisStateService()
user = user_state_service.UserStateService()

class IrisUserState(iris_user_state_pb2_grpc.IrisUserStateServicer):
    def GetIris(self, request, context):
        return iris_user_state_pb2.GetIrisResponse(
            state=iris.get(request.iris_id))

    def UpdateIris(self, request, context):
        print(request.params.value)
        iris.update(request.iris_id, request.params.value)
        return iris_user_state_pb2.UpdateIrisResponse()

    def GetUser(self, request, context):
        return user_state_pb2.GetUserResponse(
            state=user.get(request.user_id))

    def UpdateUser(self, request, context):
        user.update(request.user_id, request.params.value)
        return user_state_pb2.UpdateUserResponse()

    def UpdateUserByIris(self, request, context):
        user.update(request.user_id, iris.get(request.iris_id))
        return user_state_pb2.UpdateUserResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iris_user_state_pb2_grpc.add_IrisUserStateServicer_to_server(IrisUserState(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()