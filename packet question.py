'''
这是个0-1背包问题
'''
def pack_value(n,weight,values):
    length_w = len(weight)

    result = [[-1 for j in range(n + 1)] for i in range(length_w + 1)]

    for j in range(n+1):
        result[0][j] = 0
    for i in range(1, length_w+1):
        for j in range(1, n+1):
            result[i][j] = result[i-1][j]
            if j >= weight[i-1] and result[i][j] < result[i-1][j-weight[i-1]] + values[i-1]:
                result[i][j] = result[i-1][j - weight[i-1]] + values[i-1]
    return result[length_w][n]




n= 10
weight = [2, 6, 2, 5, 4]
values = [6, 5, 3, 4, 6]

print(pack_value(n, weight, values))