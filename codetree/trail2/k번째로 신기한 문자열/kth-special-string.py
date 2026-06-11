n, k, t = input().split()
n, k = int(n), int(k)

words = [input() for _ in range(n)]

words.sort()

cnt = 0

for word in words:
    if word.startswith(t):
        cnt += 1
        if cnt == k:
            print(word)
            break