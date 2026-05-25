n = 5
# name = []
# height = []
# weight = []

# for _ in range(n):
#     n, h, w = input().split()
#     name.append(n)
#     height.append(int(h))
#     weight.append(float(w))

class HumanInfo:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
people = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    h_i = int(h_i)
    w_i = float(w_i)
    people.append(HumanInfo(n_i, h_i, w_i))

h_people = people.copy()

people.sort(key=lambda x: x.name)
h_people.sort(key=lambda x: x.height, reverse=True)

print("name")
for i in range(n):
    print(f"{people[i].name} {people[i].height} {people[i].weight}")


print("\nheight")
for i in range(n):
    print(f"{h_people[i].name} {h_people[i].height} {h_people[i].weight}")