def solution(prices):
    answer = []
    n = len(prices)
    answer = [0] * n

    stack=[0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop() #index가 return
            answer[j] = i - j
        stack.append(i)

            # stack에 남아있는 것들은 가격 유지 혹은 오름
    while stack:
        j=stack.pop()
        answer[j]=n-1-j

    return answer