def solution(numbers):
    answer = 0
    
    s1 = {0, 1,2,3,4,5,6,7,8,9}
    numbers = set(numbers)
    s3 = s1 - numbers
    print(s3)
    
    for number in s3:
        print(number)
        answer += number
    return answer