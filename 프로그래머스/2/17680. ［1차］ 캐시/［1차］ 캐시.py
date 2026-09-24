def solution(cacheSize, cities):
    cache = []
    answer = 0

    for city in cities:
        city = city.lower()  
        if city in cache:
            cache.remove(city)  
            cache.append(city)  
            answer += 1
        else:
            if cacheSize > 0 and len(cache) >= cacheSize:
                cache.pop(0) 
            if cacheSize > 0:
                cache.append(city)
            answer += 5
    return answer
