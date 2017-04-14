num = '451'
i = int(num)
while True:
    num = str(i)
    length = len(num)
    a = num[:length//2]
    if length %2 ==0:
        b = num[length:length//2:-1]
    else:
        b = num[length:length//2+1:-1]
    if a == b:
        print(i)
        break
    i += 1