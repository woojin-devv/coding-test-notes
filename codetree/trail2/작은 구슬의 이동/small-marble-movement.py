n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# n * n 행
# t 이동 시간 
# r row
# c column 
# d direction - 초기 방향

#북 동 서 남
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

cur_dir_num = mapper[d]

def in_range(x, y, n):
    if 1 <= x and x < n+1 and 1 <= y and y < n+1:
        return True
    return False

# r + nx, c + nx의 값이 in_range인지 확인 -- 1
# in_range -> true ; x, y = r + nx, c + ny
#          -> False ; dir_num = 3 - dir_num

# 최종 -> return x, y
x, y = r, c
for i in range(t):
    # 방향 전환
    if not in_range(x + dxs[cur_dir_num], y + dys[cur_dir_num], n):
        cur_dir_num = 3 - cur_dir_num
    else: 
        x, y = x + dxs[cur_dir_num], y + dys[cur_dir_num]
    
print(x, y)
    


