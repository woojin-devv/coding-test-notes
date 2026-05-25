MAX_N = 5

codenames = []
scores = []

# Please write your code here.
class HumanInfo:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

humans = []

for _ in range(MAX_N):
    codename, score = input().split()
    humans.append(HumanInfo(codename, int(score)))

min_human = humans[0]

for i in range(MAX_N):
    if humans[i].score < min_human.score:
        min_human = humans[i]

print(min_human.codename, min_human.score)