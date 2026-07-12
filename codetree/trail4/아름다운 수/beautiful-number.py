n = int(input())

memo = {}


def count(remaining):
    # 정확히 길이를 모두 채운 경우
    if remaining == 0:
        return 1

    # 길이를 초과한 경우
    if remaining < 0:
        return 0

    if remaining in memo:
        return memo[remaining]

    result = 0

    for digit in range(1, 5):
        # digit을 선택하면 digit 길이만큼 사용
        result += count(remaining - digit)

    memo[remaining] = result
    return result


print(count(n))