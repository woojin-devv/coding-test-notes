def solution(arr, k):
    return [el + k if k % 2 == 0 else el * k for el in arr]