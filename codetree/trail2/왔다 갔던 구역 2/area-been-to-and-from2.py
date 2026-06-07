n = int(input())
results = []
current_i = 0

MAX_SIZE = 2_001
OFFSET = 1_000
results = [0] * MAX_SIZE

current = OFFSET

for _ in range(n):
    x, d = input().split()
    x = int(x) # 1: 2

    if d == "L":
        for i in range(current-1, current-x-1, -1):
            results[i] += 1
        
        current -= x 

    elif d == "R":
        for i in range(current, current+x):
            results[i] += 1
        
        current += x

count = 0

for el in results:
    if el >= 2: 
        count += 1

print(count)
