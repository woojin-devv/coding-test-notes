n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

for i in range(m):
    a_1, a_2 = queries[i]
    print(sum(arr[a_1-1:a_2]))