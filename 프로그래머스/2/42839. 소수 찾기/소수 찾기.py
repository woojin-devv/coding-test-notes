def solution(numbers):
    numbers = list(numbers)
    
    answer = 0
    answers = set()
    visited = [False] * len(numbers)
    
    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def dfs(curr):
        if curr:
            num = int(curr)

            if is_prime(num):
                answers.add(num)

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(curr + numbers[i])
                visited[i] = False

    dfs("")  # DFS 시작
    answer = len(answers)
    return answer