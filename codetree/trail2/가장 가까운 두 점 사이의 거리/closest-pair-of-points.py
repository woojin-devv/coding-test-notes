n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

def get_distance(x1, y1, x2, y2):
    return pow((x1-x2), 2) + pow((y1-y2), 2)

min_distance = float('inf')

for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        distance = get_distance(x1, y1, x2, y2)

        min_distance = min(min_distance, distance)

print(min_distance)