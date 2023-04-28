class Solution(object):
    def isHappy(self, n):
        repeat = []
        sum = n
        while sum != 1:
            t = str(sum)
            sum = 0
            for x in t:
                x = int(x)
                sum = sum +(x*x)
            if sum in repeat:
                return False
            repeat.append(sum)
        if sum == 1:
            return True

p1 = Solution()
print(p1.isHappy(19))
p2 = Solution()
print(p2.isHappy(2))