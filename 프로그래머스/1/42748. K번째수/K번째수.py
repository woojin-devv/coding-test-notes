def solution(array, commands):
    answer = []
    for row in commands:
        i = row[0]
        j = row[1]
        k = row[2]
        
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer