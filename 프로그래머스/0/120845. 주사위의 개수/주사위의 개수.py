def solution(box, n):
    answer = 0
    
    width = box[0] // n
    length = box[1] // n
    height = box[2] // n
    
    answer = width * length * height
    return answer