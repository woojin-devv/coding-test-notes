N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
sorted_b = sorted(B)

def is_beautiful(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

for i in range(N - M + 1):
    window = sorted(A[i:i + M])

    if is_beautiful(window, sorted_b):
        cnt += 1

print(cnt)