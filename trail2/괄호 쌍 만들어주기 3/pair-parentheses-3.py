A = input()
arr = list(A)

cnt = 0
for i in range(len(arr)):
    if arr[i] == "(":
        for j in range(i, len(arr)):
            if arr[j] == ")":
                cnt += 1

print(cnt)