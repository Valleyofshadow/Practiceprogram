class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        i = 0
        while i < len(nums1):
            x = 0
            while x < len(nums2):
                if nums1[i] == nums2[x]:
                    index =  x + 1
                    t = 0
                    while index < len(nums2):
                        if nums2[index] > nums2[x]:
                            ans.append(nums2[index])
                            t = 1
                            x = len(nums1)
                            break
                    if t == 0:
                        ans.append(-1)
                x += 1
            i += 1
        return ans


p1 = Solution()
print (p1.nextGreaterElement([3,1,5,7,9,2,6],[1,2,3,5,6,7,9,11]))