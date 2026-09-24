def solution(bandage, health, attacks):
    # bandage [시전 시간(t), 초당 회복량(x), 추가 회복량(y)]
    # health -> 최대 체력, 이 이상 회복 불가
    # attacks [공격 시간(t), 피해량]
    
    answer = 0
    t = attacks[-1][0]
    current_health = health
    count = 0
    
    for i in range(t+1):
        isAttacked = False
            
        for j in range(len(attacks)):
            if i == attacks[j][0]:
                isAttacked = True
                count = 0 # 누적 bandage 초기화
                current_health -= attacks[j][1]
                if current_health <= 0:
                    return -1
                
        if (not isAttacked) and current_health < health:
            current_health += bandage[1]
            if current_health > health:
                current_health = health
            count += 1
            
        if count == bandage[0]:
            count = 0
            if current_health + bandage[2] <= health:
                current_health += bandage[2]
            else:
                current_health = health
        print("시간", i, "count", count, "current_health", current_health )
    
    answer = current_health
    return answer