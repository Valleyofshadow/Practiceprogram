class Solution(object):
    def countOdds(self, low, high):
        dif = high - low
        adj = 0
        gap = 0
        even = 0
        if low % 2 == 0 :
            if high % 2 == 0:
                adj = 0
            else:
                adj = 1
        else:
            if high % 2 == 0:
                adj = 1
            else:
                adj = 1
        gap = (dif/2) + adj
        return gap
p1 = Solution
print (p1.countOdds(1,3,7))
p2 = Solution
print (p2.countOdds(1,8,10))