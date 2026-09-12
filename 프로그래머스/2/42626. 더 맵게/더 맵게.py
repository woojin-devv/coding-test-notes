from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    h = []

    for el in scoville:
        heappush(h, el)

    def get_new_scoville(n1, n2):
        return n1 + n2 * 2

    while h[0] < K:
        
        if len(h) < 2:
            return -1
        
        num1 = heappop(h)
        num2 = heappop(h)

        new_scoville = get_new_scoville(num1, num2)
        heappush(h, new_scoville)

        answer += 1

    return answer