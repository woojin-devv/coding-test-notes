n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

_max = 0
for row in grid:
    # if max < sum(row):
    #     max = sum(row)
    for i in range(len(row)-2):
        _sum = row[i] + row[i+1] + row[i+2]
        if _max < _sum:
            _max = _sum
print(_max)
