n = int(input())
nums = list(map(int, input().split()))

nums.sort()

_max = 0
for i in range(len(nums)//2):
    left, right = i, len(nums) - i - 1
    if _max < nums[left] + nums[right]:
        _max = nums[left] + nums[right]

print(_max)

# n = 2
# 2 3 5 5 

# n = 3
# 1 2 3 5 7 8
