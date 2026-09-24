import heapq

def solution(n, works):
    # 모든 작업을 끝낼 수 있는 경우
    if sum(works) <= n:
        return 0

    # 최대 힙처럼 사용하기 위해 음수로 변환
    heap = [-work for work in works]
    heapq.heapify(heap)

    for _ in range(n):
        # 가장 큰 작업량 꺼내기
        max_work = -heapq.heappop(heap)

        # 1시간 작업
        max_work -= 1

        # 다시 음수로 넣기
        heapq.heappush(heap, -max_work)

    answer = 0

    for work in heap:
        answer += work ** 2

    return answer