n = int(input())

class Student:
    count = 0
    def __init__(self, height, weight):
        Student.count += 1
        self.num = Student.count
        self.height = height
        self.weight = weight

student = []

for _ in range(n):
    height, weight = map(int, input().split())
    student.append(Student(height, weight))

student.sort(key = lambda x: (x.height, -x.weight))

for i in range(n):
    print(student[i].height, student[i].weight, student[i].num)