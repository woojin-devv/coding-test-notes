n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# check 함수 
def check_happy(arr, m):
    count = 1

    if len(arr) == 1:
        if arr[0] == m:
            return True
    else:
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                count += 1
            else:
                count = 1
            if count >= m:
                return True
    
    return False

# 행
result = 0
for i in range(n):
    if check_happy(grid[i], m):
        result += 1


# 열
for i in range(n):
    col = []
    for j in range(n):
        col.append(grid[j][i])
    
    if check_happy(col, m):
        result += 1

print(result)