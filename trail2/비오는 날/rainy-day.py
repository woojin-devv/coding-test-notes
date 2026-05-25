n = int(input())

# Please write your code here.

class WeatherInfo:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

# for _ in range(n):
#     d, dy, w = input().split()
#     date.append(d)
#     day.append(dy)
#     weather.append(w)

weathers = []

for _ in range(n):
    d, dy, w = input().split()
    weathers.append(WeatherInfo(d, dy, w))

weathers.sort(key=lambda x: x.date)

for i in range(len(weathers)):
    if weathers[i].weather == "Rain":
        print(f"{weathers[i].date} {weathers[i].day} {weathers[i].weather}")
        break