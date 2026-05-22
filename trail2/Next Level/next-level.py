user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Info1:
    def __init__(self, id="codetree", level=10):
        self.id = id
        self.level = level

class Info2:
    def __init__(self, id, level):
        self.id = id
        self.level = level

info1 = Info1()
info2 = Info2(user2_id, user2_level)

print(f"user {info1.id} lv {info1.level}")
print(f"user {info2.id} lv {info2.level}")