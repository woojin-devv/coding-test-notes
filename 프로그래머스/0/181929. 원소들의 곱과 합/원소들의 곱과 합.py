def solution(num_list):
    multiply = 1
    square = 0

    for i in num_list:
        multiply *= i

    for i in num_list:
        square += i

    if multiply < square ** 2:
        return 1
    else:
        return 0
