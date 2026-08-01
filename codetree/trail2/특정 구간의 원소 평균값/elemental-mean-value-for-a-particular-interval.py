n = int(input())
arr = list(map(int, input().split()))

answer = 0

for start in range(n):
    for end in range(start, n):
        section = arr[start:end + 1]
        total = sum(section)
        length = len(section)

        if total % length == 0:
            avg = total // length

            if avg in section:
                answer += 1

print(answer)