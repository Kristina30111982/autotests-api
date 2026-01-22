import socket


def start_server():

    host = '127.0.0.1'
    port = 12345


    message_history = []


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(10)
        print(f"Сервер запущен на {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Подключено: {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break


                    message = data.decode('utf-8')
                    message_history.append(message)


                    response = "\n".join(message_history)
                    conn.sendall(response.encode('utf-8'))


if __name__ == "__main__":
    start_server()

