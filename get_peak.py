n = int(input())
fn = input().split(' ')
tmp = []
result = []
li = []
for i in range(len(fn)):
    fn[i] = int(fn[i])

for i in range(len(fn)):  #求各个点与前一个点的差值
    if i == 0:
        tmp.append(fn[i])
    else:
        tmp.append(fn[i] - fn[i-1])
print('tmp:%s' % tmp)
for i in range(len(tmp)-1):  #
    if tmp[i] < 0 and tmp[i+1] > 0:
        result.append(i)
    if i == len(tmp) - 2 and tmp[i] <0:
        result.append(i+1)
print('result:%d' %result)
for i in range(len(result)):
    if i == 0 or i == len(result) -1:
        li.append(result[i])
    else:
        print(result[i] - result[i-1])
        li.append(result[i] - result[i-1])
print(li)
max = li.index(max(li))
l = result[max-1:max+1]
print(str(l[0]) + ' ' + str(l[1]))
