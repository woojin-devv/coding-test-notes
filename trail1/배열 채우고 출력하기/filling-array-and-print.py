arr = list(input().split())

text = ""
for i in range(len(arr)-1, -1, -1):
    text += arr[i]
print(text)