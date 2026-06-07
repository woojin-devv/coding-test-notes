a, b, c, d = map(int, input().split())

# Please write your code here.

if b < d:
    h = (c - a) * 60
    m = d - b
else:
    h = (c - a - 1) * 60
    m = (60 - b) + d

print(h+m) 