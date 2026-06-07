n = int(input())

class Point:
    def __init__ (self, i, x, y):
        self.i = i
        self.x = x
        self.y = y 
        self.distance = abs(x) + abs(y)
    
points = []

for i in range(n):
    x_i, y_i = map(int, input().split())

    points.append(Point(i+1, x_i, y_i))

points.sort(key=lambda x: x.distance)

for i in range(n):
    print(f"{points[i].i}")
