def solution(my_string, is_suffix):
    k = len(is_suffix)
    
    return 1 if my_string[-k:] == is_suffix else 0
