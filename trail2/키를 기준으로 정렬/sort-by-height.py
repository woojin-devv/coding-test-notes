n = int(input())
name = []
height = []
weight = []



# Please write your code here.

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    

people = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    people.append(Person(n_i, h_i, w_i))

people.sort(lambda x: x.height)

for i in range(n):
    print(f"{people[i].name} {people[i].height} {people[i].weight}")