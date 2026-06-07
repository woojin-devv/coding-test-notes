n, m = map(int, input().split())

_len = max(n, m)
results = []

for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        gcd = i

print(n * m // gcd)