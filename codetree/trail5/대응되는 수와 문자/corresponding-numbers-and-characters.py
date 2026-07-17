n, m = map(int, input().split())

mapping = {}

for index in range(1, n + 1):
    word = input().strip()

    mapping[index] = word
    mapping[word] = index

for _ in range(m):
    query = input().strip()

    if query.isdigit():
        query = int(query)

    print(mapping[query])