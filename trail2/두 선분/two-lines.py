x1, x2, x3, x4 = map(int, input().split())

MAX = 101
arr = [0] * MAX

for i in range(x1, x2+1):
    arr[i] += 1

for i in range(x3, x4+1):
    arr[i] += 1

def check_intersect(arr):
    if max(arr) >= 2:
        return "intersecting"
    return "nonintersecting"

print(check_intersect(arr))