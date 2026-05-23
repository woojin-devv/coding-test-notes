N = int(input())

# Please write your code here.
def re_sum(N):
    if N == 1:
        return 1
    return re_sum(N-1) + N

print(re_sum(N))