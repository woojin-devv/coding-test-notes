from collections import deque

def solution(x, y, n):
    q = deque([(y, 0)])
    visited = {y}

    while q:
        cur, cnt = q.popleft()

        if cur == x:
            return cnt

        if cur % 3 == 0:
            next_num = cur // 3
            if next_num >= x and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt + 1))

        if cur % 2 == 0:
            next_num = cur // 2
            if next_num >= x and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt + 1))

        next_num = cur - n
        if next_num >= x and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, cnt + 1))

    return -1