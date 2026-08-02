n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

max_triangle = 0

def get_triangle(x1, y1, x2, y2, x3, y3):
    return abs(
        (x1 * y2 + x2 * y3 + x3 * y1)
        - (x2 * y1 + x3 * y2 + x1 * y3)
    )

for i in range(n):
    x1, y1 = points[i]

    for j in range(i + 1, n):
        x2, y2 = points[j]

        # 첫 번째와 두 번째 점이 수평변을 만드는 경우
        if y1 == y2:
            for k in range(n):
                if k == i or k == j:
                    continue

                x3, y3 = points[k]

                # 세 번째 점이 수평변의 한 끝점과 수직으로 연결됨
                if x3 == x1 or x3 == x2:
                    triangle = get_triangle(
                        x1, y1,
                        x2, y2,
                        x3, y3
                    )

                    max_triangle = max(max_triangle, triangle)

print(max_triangle)