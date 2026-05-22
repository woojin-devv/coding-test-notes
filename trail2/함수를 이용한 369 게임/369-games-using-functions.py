a, b = map(int, input().split())

# Please write your code here.
def is_number_in_tsn(n):
    flag = False
    arr = ['3', '6', '9']
    target = list(str(n))
    for el in target:
        if el in arr :
            flag = True
    return flag

def is_number_multiple_of_three(n):
    if n % 3 == 0:
        return True
    return False

count = 0
for i in range(a, b+1):
    if is_number_in_tsn(i) or is_number_multiple_of_three(i):
        count += 1
    
print(count)
