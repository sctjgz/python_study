nq = input().split(' ')
a = input().split(' ')
b = input().split(' ')
li = []
for i in range(int(nq[1])):
    li.append(input().split(' '))
    '''for j in range(int(nq[1])):
        li[i][j] = int(li[i][j])
print(li)
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])'''
for i in range(int(nq[1])):
    count = 0
    for j in range(int(nq[0])):
        if a[j] >= li[i][0] and b[j] >= li[i][1]:
            count += 1

    print(count)