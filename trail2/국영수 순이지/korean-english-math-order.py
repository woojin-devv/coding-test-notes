n = int(input())
# name = []
# korean = []
# english = []
# math = []

# for _ in range(n):
#     student_info = input().split()
#     name.append(student_info[0])
#     korean.append(int(student_info[1]))
#     english.append(int(student_info[2]))
#     math.append(int(student_info[3]))

# # Please write your code here.

class Grade:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math 
    

grades = []

for _ in range(n):
    name, k, e, m = input().split()
    k = int(k)
    e = int(e)
    m = int(m)
    grades.append(Grade(name, k, e, m))

grades.sort(key=lambda x: (x.korean, x.english, x.math), reverse=True)

for i in range(n):
    print(f"{grades[i].name} {grades[i].korean} {grades[i].english} {grades[i].math}")