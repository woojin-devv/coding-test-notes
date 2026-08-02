n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

# i는 제외할 시간 대의 개발자

max_time = float('-inf')
for i in range(len(times)):
    a, b = times[i]
    time = []
    for j in range(len(times)):
        a2, b2 = times[j]

        if a == a2 and b == b2:
            continue
        
        else:
            for t in range(a2, b2):
                time.append(t)
            
            time = list(set(time))
            max_time = max(len(time), max_time)

print(max_time)