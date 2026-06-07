n = int(input())

# Please write your code here.
def _check_hap(n):
    if (n // 10 + n % 10) % 5 == 0:
        return True
    return False

def _check_even(n):
    if (n % 2 == 0):
        return True
    return False

if _check_hap(n) and _check_even(n):
    print("Yes")
else:
    print("No")