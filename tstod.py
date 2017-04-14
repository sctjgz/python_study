import sys

n =[]
dic = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,\
       'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
stopword = ''
for i in iter(input,stopword):
    n.append(i)
print(n)
for i in n:
    num = i[::-1]
    length = len(num)
    result = 0
    for i in range(length):
        result += dic[num[i]]* (26**i)
    print(result)