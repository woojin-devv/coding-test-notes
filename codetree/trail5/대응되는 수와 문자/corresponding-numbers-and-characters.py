n, m = map(int, input().split())
words = dict()
numbers = dict()

start = 1
for _ in range(n):
    k = input()
    words[k] = start
    numbers[start] = k
    start += 1


for _ in range(m):
    find = input()
    if find.isdigit():
        print(numbers[int(find)])
    else:
        print(words[find])