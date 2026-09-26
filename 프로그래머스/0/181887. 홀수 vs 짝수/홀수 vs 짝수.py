def solution(num_list):
    answer = 0
    odd = 0
    even = 0 
    for i in range(0, len(num_list), 2):
        print(f"odd {i}")
        odd += num_list[i]
    for i in range(1, len(num_list), 2):
        print(f"even {i}")
        even += num_list[i]

    return max(odd, even)