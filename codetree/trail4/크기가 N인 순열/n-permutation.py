n = int(input())

visited = [0] * (n + 1)
arr = []

def print_answer(arr):
    print(*arr)

def choose(curr_num):
    if curr_num == n+1:
        print_answer(arr)

    for d in range(1, n+1):
        if visited[d]: continue
        visited[d] = 1
        arr.append(d)
    
        choose(curr_num + 1)

        arr.pop()
        visited[d] = 0

choose(1)
    

