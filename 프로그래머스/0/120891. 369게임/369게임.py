from collections import Counter as counter

def solution(order):
    answer = 0
    freq = counter(str(order))

    return freq['3'] + freq['6'] + freq['9']