from collections import Counter as c

def solution(participant, completion):
    nc = c(participant) - c(completion)
    return list(nc.keys())[0]