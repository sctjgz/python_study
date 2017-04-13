import math
def NewtonSqrt(n):
    result = n
    EPS = 0.000001
    while True:
        tmp = result
        result =result/ 2 + n/(2* result)
        if abs(tmp-result)<= EPS:
            break
    return result

print(NewtonSqrt(16.54))
print(math.sqrt(16.54))