n = int(input())

name = []
# score1 = []
# score2 = []
# score3 = []

# for _ in range(n):
#     student_input = input().split()
#     name.append(student_input[0])
#     score1.append(int(student_input[1]))
#     score2.append(int(student_input[2]))
#     score3.append(int(student_input[3]))

# # Please write your code here.

class Grade:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.tot = score1 + score2 + score3

grades = []

for _ in range(n):
    n_i, s1_i, s2_i, s3_i = input().split()
    s1_i = int(s1_i)
    s2_i = int(s2_i)
    s3_i = int(s3_i)
    grades.append(Grade(n_i, s1_i, s2_i, s3_i))

grades.sort(key=lambda x: x.tot)

for i in range(n):
    print(f"{grades[i].name} {grades[i].score1} {grades[i].score2} {grades[i].score3}")