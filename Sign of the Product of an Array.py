class Solution(object):
    def arraySign(self, nums):
        sum = 1
        for x in nums:
            sum = x * sum
        if sum < 0:
            return -1
        elif sum > 1:
            return 1
        elif sum == 0:
            return 0
p1 = Solution()
print(p1.arraySign([-1,-2,-3,-4,3,2,1]))
p2 = Solution()
print(p2.arraySign([1,5,0,2,-3]))
p3 = Solution()
print(p3.arraySign([-1,1,-1,1,-1]))