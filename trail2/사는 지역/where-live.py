n = int(input())

# Please write your code here.
class HousingInfo:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region
    
housings = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    housings.append(HousingInfo(n_i, s_i, r_i))

housings.sort(key=lambda x: x.name)

print(f"name {housings[-1].name}")
print(f"addr {housings[-1].street_address}")
print(f"city {housings[-1].region}")
