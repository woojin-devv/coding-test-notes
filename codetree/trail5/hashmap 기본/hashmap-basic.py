n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

d = dict()

for el in commands:
    if el[0] == "add":
        d[el[1]] = el[2]
    elif el[0] == "find":
        if el[1] in d:
            print(d[el[1]])
        else:
            print("None")
    elif el[0] == "remove":
        d.pop(el[1])

