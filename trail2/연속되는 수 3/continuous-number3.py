
N = int(input())
arr = [int(input()) for _ in range(N)]


cnt = 0
m_cnt = 0
results = []
for i in range(N-1):
    if (arr[i] * arr[i+1]) != abs(arr[i] * arr[i+1]):
        cnt = 0
    elif (arr[i] * arr[i+1]) == abs(arr[i] * arr[i+1]):
        cnt += 1
        if m_cnt <= cnt:
            m_cnt = cnt

print(m_cnt+1)