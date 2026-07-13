n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

temp = []
answer = []
# 처음
for i in range(s1, e1 + 1):
    blocks[i-1] = 0

#[1,2]
for i in range(len(blocks)):
    if blocks[i] != 0 :
        temp.append(blocks[i])


# 다음
for i in range(s2, e2 + 1):
    temp[i-1] = 0

for i in range(len(temp)):
    if temp[i] != 0:
        answer.append(temp[i])

#남은 블록 개수 출력
print(len(answer))
# 순서대로 
for i in range(len(answer)):
    print(answer[i])