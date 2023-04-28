nums = [3,2,4]
target = 6
i = 0
while i < len(nums):
    x = len(nums) - 1
    while x >= 0:
        if i == x:
            break
        sum = nums[i] + nums[x]
        if sum == target:
            print (x, i)
            break
        x = x - 1
    i = i + 1