class Solution:
    def isPalindrome(self, x):
        x = str(x)
        rev = []
        stan = []
        for t in x:
            rev.insert(0,t)
            stan.append(t)
        if rev == stan:
            return True
        else:
            return False
p1=Solution()
print(p1.isPalindrome(121),'\n')
p2=Solution()
print(p2.isPalindrome(-121),'\n')
p3=Solution()
print(p3.isPalindrome(10),'\n')
