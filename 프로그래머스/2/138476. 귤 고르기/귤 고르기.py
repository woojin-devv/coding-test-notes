from collections import Counter as c

def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    
    c_t = c(tangerine).most_common()
    max_c = c(tangerine).most_common(1)
    _real_max = max_c[0][1]
    
    if _real_max >= k:
        return 1
    else:
        cnt = 0
        for size, count in c_t:
            k -= count
            cnt += 1

            if k <= 0:
                break

    return cnt