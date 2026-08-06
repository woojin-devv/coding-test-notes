n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

max_score = 0

for start in range(1, 4):
    stone = start
    score = 0

    for x, y, z in zip(a, b, c):
        if stone == x:
            stone = y
        elif stone == y:
            stone = x
        if stone == z:
            score += 1
    
    max_score = max(max_score, score)

print(max_score)