class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        i = 0
        arr.sort()
        dist = arr[1] - arr[0]
        while i < len(arr)-1:
            if arr[i+1]- arr[i] != dist:
                return False
            i = i + 1
        return True

p1 = Solution()
print(p1.canMakeArithmeticProgression([3,5,1]))
p2 = Solution()
print(p2.canMakeArithmeticProgression([1,2,4]))