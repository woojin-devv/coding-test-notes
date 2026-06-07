M, D = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if M <= 12 and D <= 31:
    if D <= days[M-1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")