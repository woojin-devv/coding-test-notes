def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    
    # curr - 현재피로도, cnt - 방문한 던전 수
    def dfs(curr, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if (not visited[i] 
                and curr >= dungeons[i][0]
               ):
                visited[i] = True
                
                dfs(curr - dungeons[i][1], cnt + 1)
                
                visited[i] = False
        
    dfs(k, 0)
    
    return answer