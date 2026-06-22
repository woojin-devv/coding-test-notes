n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# 1초 후  
# 1 1 2
# 3 6 5 

# 2초 후 
# 5 1 1 
# 2 3 6 


# 3초 후 
# 6 5 1
# 1 2 3

for i in range(t):
    temp_u = d[-1]
    temp_d = u[-1]
    for j in range(n-1, 0, -1):
        u[j] = u[j-1]
    u[0] = temp_u
    for j in range(n-1, 0, -1):
        d[j] = d[j-1]
    d[0] = temp_d

print(*u)
print(*d)