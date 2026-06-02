R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if grid[i][j] == "W":
            grid[i][j] = 0
        else:
            grid[i][j] = 1

# 시작점, 끝점 
# start = (0, 0)
# end = (R-1, C-1)

curr = grid[0][0]
cnt = 0 
start = grid[0][0]
end = grid[R-1][C-1]

if start == end :
    print(0)

else:
    for r1 in range(1, R-1):
        for c1 in range(1, C-1):

            if curr != grid[r1][c1]:
                for r2 in range(1+r1, R-1):
                    for c2 in range(1+c1, C-1):

                        if (grid[r1][c1] != grid[r2][c2]):
                            cnt+=1
    print(cnt)