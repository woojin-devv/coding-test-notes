from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    answer = 0
    visited = [False] * len(words)
    q.append((begin, 0))

    def can_go(word1, word2):
        cnt = 0 
        for a, b in zip(word1, word2):
            if a != b:
                cnt += 1
        return cnt == 1
    
    while q:
        curr, cnt = q.popleft()
        
        if curr == target:
            return cnt
        
        for i in range(len(words)):
            if not visited[i] and can_go(words[i], curr):
                visited[i] = True
                q.append((words[i], cnt + 1))
    return 0