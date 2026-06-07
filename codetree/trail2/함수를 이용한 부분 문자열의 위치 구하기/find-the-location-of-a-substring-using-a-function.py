text = list(input())
pattern = list(input())

k = len(pattern)
window = text[:k]

flag = True
cnt = -1

if window == pattern:
    flag = False
    print(0)

for i in range(k, len(text)):
    window.append(text[i])
    window.remove(text[i-k])
    if window == pattern:
        print(i - k + 1)
        flag = False
        break

if flag:
    print(cnt)