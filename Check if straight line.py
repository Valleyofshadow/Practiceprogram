class Solution(object):
    def checkStraightLine(self, coordinates):
        xslope = coordinates[1][0] - coordinates[0][0]
        if xslope == 0:
            for t in coordinates:
                if t[0] != coordinates[0][0]:
                    return False
            return True
        yslope = coordinates[1][1] - coordinates[0][1]
        slope = float(yslope)/float(xslope)
        listlen = len(coordinates)
        y = float(coordinates[0][1])
        x = float(coordinates[0][0])
        b = slope * x
        b = y - b
        for t in coordinates [1:]:
            y = int(slope * t[0] + b)
            if t[1] != y:
                return False
        return True





p1 = Solution()
print (p1.checkStraightLine([[0,0],[0,1],[0,-1]]))
p2 = Solution()
print (p2.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
p3 = Solution()
print (p3.checkStraightLine([[2,1],[4,2],[6,3]]))