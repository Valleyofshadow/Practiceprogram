class Solution(object):
    def average(self, salary):
        min = 1000000
        max = 1000
        sum = float(0)
        count = 0
        for x in salary:
            if x > max:
                max = x
            elif x < min:
                min = x
        for x in salary:
            if x != min:
                if x != max:
                    count = count + 1
                    sum = sum + x
        return (sum / count)
p1 = Solution
print (p1.average(1,[2000,375000,349000,9000,335000,423000,428000,484000,482000,145000,328000,72000,470000,275000,55000,448000,182000,128000,475000,368000,469000,268000,265000,397000,323000,245000,173000,460000,183000,404000,123000,248000,295000,4000,27000,281000,413000,218000]))
p2 = Solution
print (p2.average(1,[1000,2000,3000]))
