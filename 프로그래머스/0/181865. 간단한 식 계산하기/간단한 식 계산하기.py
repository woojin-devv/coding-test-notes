def solution(binomial):
    arr = binomial.split()

    a = int(arr[0])
    op = arr[1]
    b = int(arr[2])

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b