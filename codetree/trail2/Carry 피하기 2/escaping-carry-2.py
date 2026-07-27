n = int(input())
arr = [int(input()) for _ in range(n)]

# 큰수 -> 작은수로 정렬 되도록 
arr.sort(reverse=True)
answer = -1

def is_carry(num1, num2):
    for digit1, digit2 in zip(reversed(str(num1)), reversed(str(num2))):
        if int(digit1) + int(digit2) >= 10:
            return True

    return False

# i는 pivot 
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not is_carry(arr[i], arr[j]):
                if not is_carry(arr[i]+arr[j], arr[k]):
                    answer = max(answer, arr[i] + arr[j] + arr[k])

                    
print(answer)