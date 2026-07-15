n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 건너뛸 수 있는 가지 수 
skip = len(points) - 2

# distance 
answer = 0 

#스킵할 index
for skip_idx in range(1, len(points)-1):
    distance = 0
    # len의 개수만큼
    for i in range(len(points)-1):
        if i == skip_idx:
            x, y = points[i-1]
            continue
        else:
            x, y = points[i]

        if (i + 1) == skip_idx:
            next_x, next_y = points[i+2]
        else:
            next_x, next_y = points[i+1]

        curr_distance = abs(x - next_x) + abs(y - next_y)
        # print(f"i: {i}, skip_idx: {skip_idx}, curr_distance: {curr_distance}")
        distance += curr_distance
    
    if answer == 0:
        answer = distance
    
    else:
        answer = min(answer, distance)

print(answer)