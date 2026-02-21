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