A, B, C = map(int, input().split())

answer = 0

for i in range(C//A + 1):
    remaining = C - A * i
    j = remaining // B
    
    value = A * i + B * j
    answer = max(answer, value)

print(answer)