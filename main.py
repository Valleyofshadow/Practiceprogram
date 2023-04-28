bulk = []
x = 1
count = 0
sum = 0
unique = []
count1 = 0
max = 0
min = None
while x != 0:
    x = input('Input a number 1 or greater, if you are done with your inputs enter 0\n')
    x = int(x)
    sum = sum + x
    if x != 0:
        bulk.append(x)
        min = x
    count = count + 1
for x in bulk:
    if x not in unique:
        unique.append(x)
        count1 = count1 + 1
    if x > max:
        max = x
    if x < min:
        min = x
print('Total numbers entered:\n', count)
print('Input numbers: \n', sorted(bulk))
print('Sum of numbers:\n', sum)
print('There were', count1, 'unique numbers entered\n', sorted(unique))
print('Max number entered', max, 'Minimum number entered', min)