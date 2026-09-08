def solution(tickets):
    answer = []
    tickets.sort()

    visited = [False] * len(tickets)

    def dfs(current, route):
        nonlocal answer 
        
        if len(route) == len(tickets) + 1:
            answer = route.copy()
            return True

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == current:
                visited[i] = True

                route.append(tickets[i][1])

                if dfs(tickets[i][1], route):
                    return True

                route.pop()
                visited[i] = False
        return False
    
    dfs("ICN", ["ICN"])

    return answer