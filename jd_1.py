def permutation(result, str, list):
    if len(list) == 1:
        result.append(str + list[0])
    else:
        for temp_str in list:
            temp_list = list[:]
            temp_list.remove(temp_str)
            permutation(result, str + temp_str, temp_list)


def getresult(result, li):
    permutation(result, '', li[:2])
    permutation(result, '', li[1:])
    permutation(result, '', li)
    a = []
    a.append(li[0])
    a.append(li[2])
    permutation(result, '', li)
    result = [int(i) for i in result]
    result.sort()
    return result


li = input().split(' ')
result = li[:]
flag = int(li[-1]) - 1
if len(set(li)) != len(li):
    print(-1)
for i in li:
    if len(i) != 1:
        print(-1)
    if ord(i) > 57 or ord(i) < 49:
        print(-1)
if ('2' in li and '5' in li) or ('6' in li and '9' in li):
    print(-1)
result = getresult(result, li)

if '2' in li:
    li[li.index('2')] = '5'
elif '5' in li:
    li[li.index('5')] = '2'
result = getresult(result, li)

if '6' in li:
    li[li.index('6')] = '9'
elif '9' in li:
    li[li.index('9')] = '6'

result = getresult(result, li)
print(result[flag])