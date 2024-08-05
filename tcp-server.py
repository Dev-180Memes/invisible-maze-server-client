import socket
import threading

# Maze setup (0 = path, 1 = wall, E = exit)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 'E']
]
start_position = (0, 0)


# Check if move is valid and if the player has reached the exit
def check_move(position, direction):
    x, y = position
    if direction == 'up':
        x -= 1
    elif direction == 'down':
        x += 1
    elif direction == 'left':
        y -= 1
    elif direction == 'right':
        y += 1
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        if maze[x][y] == 0:
            return (x, y), "Move successful"
        elif maze[x][y] == 'E':
            return (x, y), "Exit found"
    return position, "Invalid move"


def handle_client(client_socket, address):
    print(f"Connection from {address} has been established.")
    position = start_position
    while True:
        direction = client_socket.recv(1024).decode('utf-8')
        if not direction:
            break
        position, response = check_move(position, direction)
        client_socket.send(response.encode('utf-8'))
        if response == "Exit found":
            break
    client_socket.close()


def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Server started, waiting for connections...")
    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()


if __name__ == "__main__":
    start_server()
