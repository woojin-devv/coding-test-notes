from collections import Counter as c
n = int(input())
words = [input() for _ in range(n)]

freq = c(words)

# help(sorted)
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print(freq[0][1])
