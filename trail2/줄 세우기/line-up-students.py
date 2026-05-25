n = int(input())

class Student:
    def __init__(self, number, height, weight):
        self.number = number
        self.height = height
        self.weight = weight

students = []

for i in range(n):
    h_i, w_i = map(int, input().split())
    students.append(Student(i+1, h_i, w_i))

students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for i in range(n):
    print(f"{students[i].height} {students[i].weight} {students[i].number}")