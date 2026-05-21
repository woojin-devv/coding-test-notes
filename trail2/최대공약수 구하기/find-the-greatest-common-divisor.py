n, m = map(int, input().split())

# Please write your code here.

def GCD(n, m):
    results = []
    for i in range(1, m+1):
        if n % i ==0 and m % i ==0:
            results.append(i)
    print(max(results))

GCD(n, m)