n, m = map(int, input().split())

# 거리 = 속력 x 시간 
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

tot_time = 0

for el in t:
    tot_time += el

#distance_A, B의 idx는 tot_time    
distance_A = [0] * (tot_time + 1)
distance_B = [0] * (tot_time + 1)

idx = 0 
duration = t[idx]
for time in range(1, tot_time+1):
    if time <= duration:
        distance_A[time] = v[idx] + distance_A[time - 1]
    else:
        idx += 1
        duration += t[idx]
        distance_A[time] = v[idx] + distance_A[time - 1]

idx = 0 
duration = t2[idx]
for time in range(1, tot_time+1):
    if time <= duration:
        distance_B[time] = v2[idx] + distance_B[time-1]
    else:
        idx += 1
        duration += t2[idx]
        distance_B[time] = v2[idx] + distance_B[time - 1]

# print(distance_A)
# print(distance_B)

# answer
answer = [0] * len(distance_A)

idx = 0
for i, j in zip(distance_A, distance_B):
    answer[idx] = j - i
    idx += 1

# print(answer)
cnt = 0
prev = 0

for value in answer:
    if value == 0:
        continue

    if prev != 0:
        if (prev > 0 and value < 0) or (prev < 0 and value > 0):
            cnt += 1

    prev = value

print(cnt)