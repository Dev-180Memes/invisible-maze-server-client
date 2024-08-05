import socket

# Maze setup (0 = path, 1 = wall, E = exit)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 'E']
]
start_position = (0, 0)


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


def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print("Server started, waiting for connections...")
    client_socket, address = server.accept()
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


if __name__ == "__main__":
    start_server()
