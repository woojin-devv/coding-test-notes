arr = list(map(int, input().split()))

'''
- 일단 1팀을 고른다(한명)

이후 
1. 4명중 2명을 한팀으로 만든다. 
2. 팀간의 합을 비교한다. (1팀(1명), 2팀(2명), 3팀(2명))
    2.1 팀간의 합이 같지 않을 경우 -> 최대값 및 최소값 비교
    2.2 팀간의 합이 같을 경우 -> 다시 팀 구하기 
    2.3 불가능하다면 -1 출력
'''

total_sum = sum(arr)
answer = float('inf')

for i in range(len(arr)):
    # i는 한 명의 팀. 
    t1 = arr[i]
    for j in range(len(arr)):
        for k in range(len(arr)):
            if i != j and j != k and i != k:
                #team 2
                t2 = arr[j] + arr[k]

                #team 3 
                t3 = total_sum - (t1 + t2)
                
                # 모든 팀의 능력치가 서로 달라야함. 
                
                if t1 != t2 and t1 != t3 and t2 != t3:
                    max_ab = max(t1, t2, t3)
                    min_ab = min(t1, t2, t3)

                    gap = abs(max_ab - min_ab)

                    answer = min(gap, answer)

if answer != float('inf'):
    print(answer)
else:
    print(-1)