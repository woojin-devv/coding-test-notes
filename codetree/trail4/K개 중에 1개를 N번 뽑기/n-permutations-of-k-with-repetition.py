K, N = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num, K):
    if curr_num == N + 1:
        print_answer()
        return

    for i in range(1, K + 1):
        answer.append(i)
        choose(curr_num + 1, K)
        answer.pop()

    return

choose(1, K)