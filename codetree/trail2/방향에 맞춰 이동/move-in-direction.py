n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x = 0 
y = 0

dx = 0 
dy = 0 

for i in range(n):
    if dir[i] == "N":
        dy += dist[i]
    elif dir[i] == "E":
        dx += dist[i]
    elif dir[i] == "W":
        dx -= dist[i]
    elif dir[i] == "S":
        dy -= dist[i]

print(dx, dy)


