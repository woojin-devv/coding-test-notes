binary = input()

result = 0
arr = list(binary)

for i in range(len(arr)):
    result += int(arr[i]) * pow(2, len(arr)-1-i)

print(result)