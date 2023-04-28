class Solution(object):
    def nearestValidPoint(self, x, y, points):
        valid =[]
        mindist = 100
        c = 0
        closet = None
        for t,z in points:
            if t == x or z == y:
                valid.append([t,z,c])
            c = c + 1
        for t,z,c in valid:
            dist = (abs(x-t) + abs(y-z))
            if dist < mindist:
                mindist = dist
                closet = c
        if closet == None:
            closet = -1
        return closet

p1 = Solution()
print (p1.nearestValidPoint(3, 4,[[1,2,],[3,1],[2,4],[2,3],[4,4]] ))
p2 = Solution()
print (p2.nearestValidPoint(3,4,[[3,4]]))
p3 = Solution()
print (p3.nearestValidPoint(1, 1,[[1,1], [1,1]]))