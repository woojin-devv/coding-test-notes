n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [0] * (n+1)

for i in range(k):
    x, y = commands[i]

    for i in range(x, y+1):
        arr[i] += 1

print(max(arr))