class Solution(object):
    def firstUniqChar(self, s):
        t= 1
        exclude = []
        count = 0
        failed = 0
        for i in s:
            for x in s[t:]:
                #rint (i, x)
                if i in exclude:
                    break
                elif i == x:
                    exclude.append(i)
                    break
            t = t + 1
        #print (exclude)
        for i in s:
            if i in exclude:
                #print (count, i, 'fail')
                failed = failed + 1
            else:
                #print(count, i, 'pass')
                return int(count)
            count = count + 1
            if failed == len(s):
                return int(-1)




p1 = Solution()
print(p1.firstUniqChar('leetcode'))
print('\n')
p2 = Solution()
print(p2.firstUniqChar('loveleetcode'))
print('\n')
p3 = Solution()
print (p3.firstUniqChar('aabb'))