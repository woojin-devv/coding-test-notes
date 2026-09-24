def solution(schedules, timelogs, startday):
    answer = 0
    
    # 월요일을 0으로 맞춤
    startday -= 1
    
    for i in range(len(schedules)):
        # i번째 직원의 희망 출근 시간을 분으로 변환
        schedule = schedules[i]
        
        hour = schedule // 100
        minute = schedule % 100
        
        limit = hour * 60 + minute + 10
        
        success = True
        
        for j in range(7):
            day = (startday + j) % 7
            
            if day == 5 or day == 6:
                continue
            
            log = timelogs[i][j]
            
            log_hour = log // 100
            log_minute = log % 100
            
            arrival = log_hour * 60 + log_minute
            
            if arrival > limit:
                success = False
                break
        
        if success:
            answer += 1
    
    return answer