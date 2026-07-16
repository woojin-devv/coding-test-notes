def solution(s):
    answer = []
    _list = []
    #1. 공백을 기준으로 문자열을 나누어 리스트에 저장
    _list = s.split(" ")
    print(_list)
    #2. 각 단어의 첫 글자를 대문자로 바꾸고 나머지 글자는 소문자로 바꾼다.
    for i in range(len(_list)):
        if _list[i]:
            _list[i] = _list[i][0].upper() + _list[i][1:].lower()
    #3. 리스트를 다시 문자열로 합쳐서 반환한다.
    answer = ' '.join(_list)
    return answer