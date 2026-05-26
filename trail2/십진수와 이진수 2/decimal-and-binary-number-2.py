N = input()

arr = list(N)
dec = 0 

for i in range(len(arr)):
    dec += int(arr[i]) * pow(2, len(arr)-i-1)

dec *= 17
digits = []

while True:
    if dec < 2:
        digits.append(dec)
        break
    digits.append(dec % 2)
    dec //= 2

for digit in digits[::-1]:
    print(digit, end="")