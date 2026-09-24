n = int(input())
commands = []
d = dict()

for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        d[k] = v
    elif cmd == "find":
        if k not in d:
            print("None")
        else:
            print(d[k])
    elif cmd == "remove":
        d.pop(k)


