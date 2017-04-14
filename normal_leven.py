'''
字符串的编辑距离：
    一个字符串通过插入和删除得到另一个字符串的最少次数
'''
def normal_leven(s1, s2):
    length_1 = len(s1)
    length_2 = len(s2)
    edit = [[0 for j in range(length_2+1)] for i in range(length_1+1)]

    for i in range(length_1+1):
        edit[i][0] = i
    for j in range(length_2+1):
        edit[0][j] = j

    for i in range(1, length_1+1):
        for j in range(1, length_2+1):
            if s1[i-1] == s2[j-1]:
                edit[i][j] = edit[i-1][j-1]
            else:
                edit[i][j] = min(edit[i-1][j], edit[i][j-1]) + 1
    return edit[length_1][length_2]


a = input('请输入第一个字符串：')
b = input('请输入第二个字符串：')
print('编辑距离是:%d' % normal_leven(a, b))