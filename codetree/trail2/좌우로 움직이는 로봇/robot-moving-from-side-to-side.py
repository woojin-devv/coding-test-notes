n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []

for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# 총 이동한 시간 
tot_time = 0 
tot_time += max(sum(t), sum(t_b))
# print(tot_time)

# position_a, position_b
position_a = [0] * (tot_time + 1)
position_b = [0] * (tot_time + 1)

def write_position(t, d, tot_time, pos_arr):
    duration, curr_pos, curr_time = 0, 0, 1
    for ta, ca in zip(t, d):
        duration += ta
        while curr_time <= duration:
            if curr_time > tot_time:
                break
            if ca =='L':
                curr_pos -= 1
            elif ca == 'R':
                curr_pos += 1
            pos_arr[curr_time] = curr_pos
            prev = curr_pos
            curr_time += 1
            # print(f"curr_time: {curr_time}, duration: {duration}")

    # 다른 로봇이 움직이는 동안, 현재 위치 누적
    if duration < tot_time:
        remain_offset = len(pos_arr) - duration
        for i in range(curr_time, curr_time + remain_offset - 1):
            pos_arr[i] = prev

    
# A 배열 기록 
write_position(t, d, tot_time, position_a)

# B 배열 기록
write_position(t_b, d_b, tot_time, position_b)

# print(position_a)
# print(position_b)
# print(len(position_a) == len(position_b))

cnt = 0
for i in range(1, len(position_a)):
    prev_a, prev_b = 0, 0 
    
    if position_a[i] == position_b[i] and position_a[i-1] != position_b[i-1]:
        cnt += 1 

print(cnt)