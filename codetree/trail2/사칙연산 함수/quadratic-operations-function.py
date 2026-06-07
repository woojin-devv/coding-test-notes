a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calc(a, o, c):
    if o == '+':
        print(f"{a} {o} {c} = {a + c}")
    elif o == '-':
        print(f"{a} {o} {c} = {a - c}")
    elif o == '/': 
        print(f"{a} {o} {c} = {int(a / c)}")
    elif o == '*':
        print(f"{a} {o} {c} = {a * c}")
    else:
        print("False")

calc(a, o, c)