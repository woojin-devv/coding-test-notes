# 2.4 내장함수를 이용한 연산
## `pow()` 함수
> pow는 거듭제곱(power)를 하겠다는 의미

```python
print( 3 ** 5 )
print( pow(3, 5) )
```

### 모듈러 거듭제곱 (3개 인자)

```python
pow(a, b, m)   # (a^b) % m
```
- 의미 : $(a^b)$ $\text{mod}$ $m$
- 빠른 거듭 제곱을 사용하여 O(log b)의 시간 복잡도를 가짐

## 구간합 > 합 배열 만들기 
```python
temp = i
numbers = list(map(int, input().split()))
prefix_sum[0]

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)
```

## 1. Counter 클래스 
> Counter는 Python의 Colletions 모듈에 포함된 클래스 중 하나.
> - 반복 가능한(iterable) 객체의 요소 개수를 손쉽게 셀 수 있도록 설계 됨. 
> - 기본적인 딕셔너리 형태로 동작 
> - 각 요소를 key, value로 저장

```python 
from collections import Counter

fruits = []

```