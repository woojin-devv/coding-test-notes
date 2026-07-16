from collections import Counter as c

n = int(input())
words = [input() for _ in range(n)]

freq = c(words)
most_b = freq.most_common(1)

print(most_b[0][1])
