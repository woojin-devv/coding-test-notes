n = int(input())
numbers = list(map(int, input().split()))

max_value = float('-inf')

# i는 pivot (고정된 값)
for i in range(n):
    for j in range(n):
        if i != j and abs(i - j) != 1:
            max_value = max(max_value, numbers[i]+ numbers[j])

print(max_value)