n = int(input())

# Please write your code here.
def print_number(n):
    if n == 0:
        return
    print_number(n-1)
    print(n, end=" ")

def print_number2(n):
    if n == 0:
        return
    print(n, end=" ")
    print_number2(n-1)

print_number(n)
print()
print_number2(n)