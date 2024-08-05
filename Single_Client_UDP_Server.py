import socket

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
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print("UDP Server started.")
    position = start_position
    while True:
        data, client_address = server.recvfrom(1024)
        direction = data.decode('utf-8')
        position, response = check_move(position, direction)
        server.sendto(response.encode('utf-8'), client_address)
        if response == "Exit found":
            break

if __name__ == "__main__":
    start_server()
