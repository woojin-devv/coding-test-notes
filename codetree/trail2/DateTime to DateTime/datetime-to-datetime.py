a, b, c = map(int, input().split())

day = 11
hour = 11
mins = 11

elapsed_time = 0

def check_prev(a, b, c):
    if a < 11:
        return True
    
    elif a == 11 and b < 11:
        return True
    
    elif a == 11 and b == 11 and c < 11:
        return True
    
    return False

if not check_prev(a,b,c):
    while True:
        if day == a and hour == b and mins == c:
            break
            
        elapsed_time += 1
        mins += 1

        if mins == 60:
            hour += 1
            mins = 0
        
        if hour == 24:
            day += 1
            hour = 0 
    
    print(elapsed_time)
        
else:
    print(-1)