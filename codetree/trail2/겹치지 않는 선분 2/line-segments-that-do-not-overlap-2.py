n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer_lines = lines.copy()

lines.sort()


def is_overlapped(line1, line2):
    x1, x2 = line1
    x3, x4 = line2

    if (
        (x1 < x3) and (x4 <= x2)
        or (x1 > x3) and (x4 >= x2)
        ):
        return True
    return False

cnt = 0 
# i는 겹치는지 확인할 target line
for i in range(len(lines)):
    flag = False
    for j in range(len(lines)):
        if lines[i] == lines[j]:
            continue

        if is_overlapped(lines[i], lines[j]):
            flag = True
            break

    if not flag:
        cnt += 1

print(cnt)