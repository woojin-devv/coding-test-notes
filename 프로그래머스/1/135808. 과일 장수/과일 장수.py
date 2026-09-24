def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    # print(f"sorted score: {score}")
    idx = 0
    while idx + m<= len(score):
        # idx = 0 부터, offset m만큼
        answer += min(score[idx:idx+m]) * m
        idx += m
    return answer