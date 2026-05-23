N = int(input())

# Please write your code here.
def print_number(N):
    if N == 0:
        return 
    print(N, end=" ")
    print_number(N-1)
    print(N, end=" ")
print_number(N)