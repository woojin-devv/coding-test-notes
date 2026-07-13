n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
temp = []
locations = []
answer = 0

def in_range(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

def bomb_one(x, y):
    temp.append((x, y))
    temp.append((x-2, y))
    temp.append((x-1, y))
    temp.append((x+1, y))
    temp.append((x+2, y))

def bomb_two(x, y):
    temp.append((x, y))
    temp.append((x-1, y))
    temp.append((x+1, y))
    temp.append((x, y+1))
    temp.append((x, y-1))

def bomb_three(x, y):
    temp.append((x, y))
    temp.append((x-1, y-1))
    temp.append((x-1, y+1))
    temp.append((x+1, y-1))
    temp.append((x+1, y+1))

def init():
    for _ in range(5):
        temp.pop()


def choose(idx):
    global answer

    if idx == len(locations):
        valid = set((a, b) for a, b in temp if in_range(a, b))
        answer = max(answer, len(valid))
        return
    
    x, y = locations[idx]

    bomb_one(x, y)
    choose(idx + 1)
    init()

    bomb_two(x, y)
    choose(idx + 1)
    init()

    bomb_three(x, y)
    choose(idx + 1)
    init()


def find_location(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                locations.append((i, j))

find_location(grid)
choose(0)
print(answer)