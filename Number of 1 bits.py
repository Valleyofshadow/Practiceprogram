class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n>0:
            if n % 2 == 1:
                count += 1
            n = n/2
        return count
p1 = Solution
print(p1.hammingWeight(00000000000000000000000000001011))
p2 = Solution
print(p2.hammingWeight(000000000000))
p3 = Solution
print(p3.hammingWeight(11111111111111111111111111111101))
