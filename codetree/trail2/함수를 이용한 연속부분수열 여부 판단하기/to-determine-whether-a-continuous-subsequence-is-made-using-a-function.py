n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = n2
window = a[:k]
answer = window
flag = False

if window == b:
    flag = True

for i in range(k, n1):
    window.append(a[i])
    window.remove(a[i-k])
    if window == b:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")