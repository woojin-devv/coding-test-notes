A = input()

# Please write your code here.
def check_p(A):
    check = False
    for i in range(len(A) // 2):
        if A[i] == A[len(A) - i -1] :
            check = True
        else:
            check = False 
    return check

if check_p(A):
    print("Yes")
else:
    print("No")