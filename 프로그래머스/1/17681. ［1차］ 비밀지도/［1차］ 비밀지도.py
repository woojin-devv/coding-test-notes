def solution(n, arr1, arr2):
    answer = []
    temp = []
    
    for a, b in zip(arr1, arr2):
        temp.append(a | b)

    def dec_to_bin(num):
        _bin = ''

        while num > 0:
            _bin += str(num % 2)
            num //= 2

        return _bin[::-1]
    
    def get_map(n, arr):
        nonlocal answer
        temp = []
        
        # binary 기반 map으로 변경
        for el in arr:
            _bin = dec_to_bin(el)
            str_bin = str(_bin).zfill(n)
            arr_bin  = list(str_bin)
            temp.append(arr_bin)
        
        for row in temp:
            bit = ''
            for el in row:
                if el == '1':
                    bit += '#'
                else:
                    bit += ' '
            answer.append(bit)
            
    get_map(n, temp)
    
    return answer