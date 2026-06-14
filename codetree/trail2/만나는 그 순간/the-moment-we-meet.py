n, m = map(int, input().split())

d = []
t = []

# A가 이동
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []

# B가 이동
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))


total_time = sum(t)

time_arr_a = [0] * total_time
time_arr_b = [0] * total_time

# A

start = 0 
for i in range(n):
    for j in range(start, start + t[i]):
        if j == 0:
            prev = 0
        else:
            prev = time_arr_a[j-1]
        if d[i] == 'R':
            time_arr_a[j] = prev + 1
        elif d[i] == 'L':
            time_arr_a[j] = prev - 1
    start += t[i]

start2 = 0 

for i in range(m):
    for j in range(start2, start2 + t2[i]):
        if j == 0:
            prev = 0
        else:
            prev = time_arr_a[j-1]
        if d2[i] == 'R':
            time_arr_b[j] = time_arr_b[j-1] + 1
        elif d2[i] == 'L':
            time_arr_b[j] = time_arr_b[j-1] - 1
            
    start2 += t2[i]

result = -1
for idx in range(1, total_time):
    if time_arr_a[idx] == time_arr_b[idx]:
        result = idx + 1
        break

print(result)