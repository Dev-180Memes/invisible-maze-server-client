import socket


def start_client(host='127.0.0.1', port=65432):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connected to the server.")
    while True:
        direction = input("Enter move (up, down, left, right): ")
        client.send(direction.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(response)
        if response == "Exit found":
            print("You won!")
            break
    client.close()


if __name__ == "__main__":
    start_client()
