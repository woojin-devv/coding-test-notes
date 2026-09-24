n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# x좌표를 dictionary의 key값으로 둠
d = dict()
answer = 0

for i in range(n):
    x, y = points[i]

    if not x in d:
        d[x] = y
    else:
        if d[x] > y:
            d.pop(x)
            d[x] = y

for value in d.values():
    answer += value

print(answer)