n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    

people = []

for i in range(n):
    n_i, h_i, w_i = input().split()
    h_i = int(h_i)
    w_i = int(w_i)
    people.append(Person(n_i, h_i, w_i))

people.sort(key=lambda x: (x.height, -x.weight))

for i in range(n):
    print(f"{people[i].name} {people[i].height} {people[i].weight}")