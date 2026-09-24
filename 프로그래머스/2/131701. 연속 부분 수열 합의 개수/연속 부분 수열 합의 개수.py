def sliding_window(k, arr):
    # 원형 수열임에 유의 - index를 len(arr)로 나눈 나머지로 처리하기
    temp = []
    # 첫 번째 window, temp 배열에 저장 
    window = sum(arr[:k])
    temp.append(window)

    #for문 돌 때, len(arr)만큼
    for i in range(len(arr)):
        next = (i + k) % len(arr)
        window += (arr[next] - arr[i])
        # print(f"k= {k}일 때, i = {i}, temp = {temp}")
        temp.append(window)
    return temp

def solution(elements):
    answer = []
    
    for i in range(1, len(elements)+1):
        temp = sliding_window(i, elements)
        answer.extend(temp)
        # print(f"temp: {temp}")
        
    answer_set = set(answer)
    result = len(answer_set)
    
    return result




