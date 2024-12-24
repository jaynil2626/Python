# file 1: ABCD,,, file2:EFGH,, output in file 3:AEBFCGDH

f1=open('self.txt')
f2=open('xyz.txt')
f3=open('abc.txt','w')
l1=f1.readlines()
l2=f2.readlines()
x=max(len(l1),len(l2))
for i in range(0,x):
    if i<len(l1):
        f3.write(f"{l1[i]}")
    if i<len(l2):
        f3.write(f"{l2[i]}")