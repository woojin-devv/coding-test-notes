Y, M, D = map(int, input().split())

def leap_year(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        return True
    return False

def check_season(M):
    if 3 <= M <= 5:
        print("Spring")
    elif 6 <= M <= 8:
        print("Summer")
    elif 9 <= M <= 11:
        print("Fall")
    else:
        print("Winter")

if leap_year(Y):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if D <= days[M-1]:
    check_season(M)
else:
    print(-1)

            
            
            