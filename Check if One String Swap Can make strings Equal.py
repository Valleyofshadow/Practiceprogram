class Solution(object):
    def areAlmostEqual(self, s1, s2):
        i = 0
        t = 0
        z = 0
        found = 0
        match = []
        i = 0
        while i < len(s1)-1:
            if s1[i] != s2[i]:
                if s1[i] in s2:
                    while z < len(s2)-1:
                        if s2 [z] == s1 [i]:
                            match.append(z)
                        z = z + 1
                    for x in match:
                        z = 0
                        if s1[x] == s2[i]:
                            found = 1
                            y = x
                    if found != 1:
                        return False
                    elif found == 1:
                        #s2[y] = s2[i]# need to set s2[y] to be s2 [i]
                        s2 = s2[:y] + s2[i] + s2[y:]
                    else:
                        t = t + 1
                    if t == 2:
                        return False
                else:
                    return False
            i = i + 1
        return True

p1 = Solution()
print (p1.areAlmostEqual("siyolsdcjthwsiplccjbuceoxmpjgrauocx", "siyolsdcjthwsiplccpbuceoxmjjgrauocx"))
p2 = Solution()
print (p2.areAlmostEqual("attack", "defend"))
p3 = Solution()
print (p3.areAlmostEqual("abcd", "dcba"))