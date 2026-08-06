n = int(input())
arr = list(map(int, input().split()))

'''
1. arr의 el 중 하나의 원소를 선택해 2배를 한다. 
2. 1번을 진행한 new arr중 하나의 숫자를 제거한다. 
    - 인접한 숫자 간의 합의 최소 값을 구한다. 
'''

min_gap = float('inf')
# i는 2배할 원소의 index
for i in range(len(arr)):
    temp = arr.copy()
    temp[i] *= 2

    #j는 제거할 원소의 index
    for j in range(len(temp)):
        new_temp = temp.copy()
        new_temp.pop(j)

        gap = 0
        for k in range(len(new_temp)-1):
            gap += abs(new_temp[k] - new_temp[k+1])
        
        min_gap = min(min_gap, gap)

print(min_gap)