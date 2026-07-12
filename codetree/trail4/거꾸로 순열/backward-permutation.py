n = int(input())
arr = []
visited = [0] * (n+1)

def print_answer(arr):
    print(*arr)

def choose(curr_num):
    if len(arr) == n:
        print_answer(arr)

    for d in range(n, 0, -1):
        if visited[d]: continue
        arr.append(d)
        visited[d] = 1

        choose(curr_num - 1)

        arr.pop()
        visited[d] = 0

choose(n)