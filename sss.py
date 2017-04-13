import math
li = input().split(' ')
result = 0
li[0] = int(li[0])
for i in range(int(li[1])):
    result += li[0]
    li[0] = math.sqrt(li[0])
    print(result)
print('%.2f' % result)
