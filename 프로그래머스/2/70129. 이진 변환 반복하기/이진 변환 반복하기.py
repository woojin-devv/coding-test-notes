def solution(s):
    transform_count = 0
    zero_count = 0

    while s != "1":
        zero_count += s.count("0")
        s = s.replace("0", "")
        length = len(s)
        s = bin(length)[2:]

        transform_count += 1

    return [transform_count, zero_count]