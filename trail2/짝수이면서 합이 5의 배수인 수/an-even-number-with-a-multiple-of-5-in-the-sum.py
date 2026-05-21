n = int(input())

# Please write your code here.
def _check(n):
    hap = n // 10 + n % 10
    if n % 2 == 0 and hap % 5 == 0:
        print("Yes")
    else:
        print("No")

_check(n)