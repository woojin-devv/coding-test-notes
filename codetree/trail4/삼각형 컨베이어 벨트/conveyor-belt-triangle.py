n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# l의 last -> r의 first 
# r의 last -> d의 first
# d의 last -> l의 first

for _ in range(t):
    # temp는 각각의 last
    temp_l, temp_r, temp_d = l[-1], r[-1], d[-1]

    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
    l[0] = temp_d

    for i in range(n-1, 0, -1):
        r[i] = r[i-1]
    r[0] = temp_l

    for i in range(n-1, 0, -1):
        d[i] = d[i-1]
    d[0] = temp_r

print(*l)
print(*r)
print(*d)