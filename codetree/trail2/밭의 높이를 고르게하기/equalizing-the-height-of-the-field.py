N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

prices = []
for el in arr:
    # abs값 price에 append
    price = abs(el - H)
    prices.append(price)

# prices 중에 T만큼 min 구해서 출력
window = sum(prices[:T])
min_value = window

for i in range(T, len(prices)):
    window += (prices[i] - prices[i-T])
    min_value = min(min_value, window)

print(min_value)
