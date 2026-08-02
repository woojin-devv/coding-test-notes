n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_square = float('inf')

# i번째 점을 제외
for i in range(n):
    arr = []

    for j in range(n):
        if i == j:
            continue

        arr.append(points[j])

    xl = min(arr, key=lambda p: p[0])[0]
    xr = max(arr, key=lambda p: p[0])[0]
    yl = min(arr, key=lambda p: p[1])[1]
    yr = max(arr, key=lambda p: p[1])[1]

    width = xr - xl
    height = yr - yl
    square = width * height

    min_square = min(min_square, square)

print(min_square)