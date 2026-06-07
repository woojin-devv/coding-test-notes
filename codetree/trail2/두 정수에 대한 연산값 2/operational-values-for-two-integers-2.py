a, b = map(int, input().split())

# Please write your code here.
def func(a, b):
    if a < b:
        a += 10
        b *= 2
    else:
        a *= 2
        b += 10
    return a, b

print(*func(a, b))