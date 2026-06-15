m1, d1, m2, d2 = map(int, input().split())

WEEK = 7
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def get_days(month, day):
    total = 0
    
    for m in range(1, month):
        total += months[m]
    
    total += day
    return total

start = get_days(m1, d1)
end = get_days(m2, d2)

diff = end - start

idx = diff % WEEK

print(week[idx])