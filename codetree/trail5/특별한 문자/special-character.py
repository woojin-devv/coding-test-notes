from collections import Counter

s = input()

freq = Counter(s)

answer = "None"

for ch in s:
    if freq[ch] == 1:
        answer = ch
        break

print(answer)