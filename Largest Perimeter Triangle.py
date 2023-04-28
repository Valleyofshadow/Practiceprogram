class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        print(nums)
        i = len(nums)-3
        while i >= 0:
            #print(nums[i],nums[i+1],nums[i+2])
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums [i+1] + nums[i+2]
            i = i - 1
            if i < 0:
                return 0

p1 = Solution()
print(p1.largestPerimeter([3,6,2,3]))
p1 = Solution()
print(p1.largestPerimeter([1,2,1,10]))