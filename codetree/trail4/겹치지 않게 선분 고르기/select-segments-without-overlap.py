n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

'''
핵심 아이디어 
선분이 n개 있을 때, 각 선분마다 선택지는 두 가지 
    1. 현재 선분을 선택한다
    2. 현재 선분을 선택하지 않는다
    => 모든 조합을 탐색, 선택한 선분끼리 겹치지 않는 경우에만 개수를 갱신

재귀함수에 입력받을 파라미터 
    - points의 index
    - selected 지금까지 선택한 선분 목록

        선분들을 입력받는다.
        answer를 0으로 초기화한다.
        현재 선택된 선분을 저장할 배열을 만든다.
        index번째 선분을 선택하지 않는 재귀를 호출한다.
        현재 선분이 기존 선택된 선분들과 겹치지 않는지 검사한다.
        겹치지 않으면 현재 선분을 추가한다.
        다음 인덱스로 재귀 호출한다.
        재귀가 끝나면 추가했던 선분을 제거한다.
        
        
        모든 선분을 확인하면 선택 개수로 최댓값을 갱신한다.
'''

def is_overlap(current, selected):
    p1, p2 = current

    for i in range(len(selected)):
        p3, p4 = selected[i]
        if max(p1, p3) <= min(p2, p4):
            return True
    return False


def backtracking(index, selected):
    global answer

    if index == n:
        answer = max(answer, len(selected))
        return

    backtracking(index + 1, selected)

    current = points[index]

    if not is_overlap(current, selected):
        selected.append(current)
        backtracking(index + 1, selected)
        selected.pop()

backtracking(0, [])
print(answer)

