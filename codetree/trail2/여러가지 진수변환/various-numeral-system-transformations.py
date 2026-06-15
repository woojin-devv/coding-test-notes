N, B = map(int, input().split())

if N == 0:
    print(0)
else:
    result = ""

    while N > 0:
        result = str(N % B) + result
        N //= B

    print(result)