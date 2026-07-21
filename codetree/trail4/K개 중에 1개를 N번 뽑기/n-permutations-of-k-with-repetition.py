k, n = map(int, input().split())

def print_answer(arr):
    print(*arr)

def backtracking(start, temp):

    if len(temp) == n:
        print_answer(temp)
        return 
    
    for i in range(1, k+1):
        temp.append(i)
        backtracking(i, temp)
        temp.pop()
        
backtracking(1, [])
