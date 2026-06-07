n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
temp = []
t_i = 0

for i in range(n):
    temp.append(arr[i])
    if (i+1) % 2 != 0:
        temp.sort()
        t_i = (len(temp)-1) // 2
        print(temp[t_i], end=" ")
        