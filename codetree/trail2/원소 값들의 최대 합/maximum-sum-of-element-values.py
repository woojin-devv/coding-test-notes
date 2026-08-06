n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_moves = float('-inf')

for idx in range(1, len(arr)):
    moves = 0
    cnt = 0
    while True:
        if cnt == m:
            break
        
        # moves
        el = arr[idx]
        moves += el
        idx = el
        cnt += 1
    
    max_moves = max(max_moves, moves)
print(max_moves)