import socket
import time


def start_client():
    host = '127.0.0.1'
    port = 12345


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        messages = ["Привет!", "Как дела?"]

        for msg in messages:
            print(f"Отправка: {msg}")
            s.sendall(msg.encode('utf-8'))

            data = s.recv(1024)
            print(f"Получено от сервера:\n{data.decode('utf-8')}")
            print("-" * 20)
            time.sleep(1)


if __name__ == "__main__":
    start_client()



