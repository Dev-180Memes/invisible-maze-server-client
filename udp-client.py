import socket


def start_client(host='127.0.0.1', port=65432):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)
    print("Connected to the server.")
    while True:
        direction = input("Enter move (up, down, left, right): ")
        client.sendto(direction.encode('utf-8'), server_address)
        response, _ = client.recvfrom(1024)
        print(response.decode('utf-8'))
        if response.decode('utf-8') == "Exit found":
            print("You won!")
            break


if __name__ == "__main__":
    start_client()
