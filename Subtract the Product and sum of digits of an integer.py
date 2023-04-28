class Solution(object):
    def subtractProductAndSum(self, n):
        sep = str (n)
        sum = 0
        pro = 1
        for x in sep:
            t = int(x)
            sum = sum + t
            pro = pro * t
        return pro - sum

p1 = Solution()
print(p1.subtractProductAndSum(234))
p2 = Solution()
print(p2.subtractProductAndSum(4421))