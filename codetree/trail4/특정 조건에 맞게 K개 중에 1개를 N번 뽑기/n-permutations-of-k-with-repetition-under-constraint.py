K, N = map(int, input().split())
arr = []

def print_answer(arr):
    print(*arr)

def choose():
    if len(arr) == N:
        print_answer(arr)
        return 

    for d in range(1, K + 1): 
        if len(arr) >= 2 and arr[-1] == d and arr[-2] == d:
            continue

        arr.append(d)
        choose()
        arr.pop()

choose()