n, k = map(int, input().split())
xs = []
cs = []

for _ in range(n):
    pos, char = input().split()
    xs.append(int(pos))
    cs.append(char)
space = max(xs)
temp = [0] * (space + 1) 

for x, c in zip(xs, cs):
    if c == 'G':
        temp[x] = 1
    elif c == 'H':
        temp[x] = 2

window = sum(temp[0:k + 1])
answer = window

for i in range(k + 1, len(temp)):
    window += (temp[i] - temp[i-k-1])
    answer = max(window, answer)
    
print(answer)