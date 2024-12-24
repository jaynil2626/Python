# IMP IN 3 or 6 marks
# a line should contain atmost 80 words, if exceed than in another line
f1=open('self.txt')
f2=open('xyz.txt','w')
l1=f1.read().split(" ")
c=0
for i in l1:
    if (c + len(i)) <= 80:
        f2.write(i+' ')
    else: 
        f2.write('\n'+i+' ')
        c=len(i)
    c+=len(i)+1