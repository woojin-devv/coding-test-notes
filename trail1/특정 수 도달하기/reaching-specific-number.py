arr = list(map(int, input().split()))
hap = 0
count = 0
for element in arr:
    if element >= 250:
        break
    hap += element 
    count += 1

avg = round(hap / count, 1)
print(hap, avg)