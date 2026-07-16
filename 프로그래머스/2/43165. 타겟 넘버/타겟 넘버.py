
# result 배열에 방문 처리 되어 가진 값을 append
result = []

def dfs(start, curr_sum, arr):
    for i in range(start, len(arr)):
        # 방문 처리된 값을 *2 만큼 뺌.
        curr_sum -= (arr[i] * 2)
        result.append(curr_sum)
    
        dfs(i+1, curr_sum, arr)
        
        curr_sum += (arr[i] * 2)
        
    return result

def solution(numbers, target):
    cnt = 0 
    # 초기 합 
    init_sum = sum(numbers)
    
    # result 배열에서 target을 찾아 count += 1
    result = dfs(0, init_sum, numbers)
    
    # 모두 양수인 경우 
    result.append(init_sum)
    
    for el in result:
        if el == target:
            cnt += 1 
            
    return cnt