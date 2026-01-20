import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc

class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f'Получен запрос к методу GetUser от пользователя: {request.username}')
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()