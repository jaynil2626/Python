# Fraction code IMP for 3 Marks
class fraction:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return str(self.x)+"/"+str(self.y)
        
    def __add__(self,other):
        x=self.x*other.y + self.y*other.x
        y=self.y*other.y
        print(self.x,self.y)
        print(other.x,other.y)
        return str(x)+"/"+str(y)

    def __sub__(self,other):
        x=self.x*other.y - self.y*other.x
        y=self.y*other.y
        return str(x) +"/"+str(y)

    def __mul__(self,other):
        x=self.x*other.x
        y=self.y*other.y
        return str(x) +"/"+ str(y)

    def __truediv__(self,other):
        x=self.x*other.y
        y=self.y*other.x
        return str(x) +"/"+ str(y)
        
f1=fraction(4,4)
f2=fraction(2,4)

print(f1)
print(f2)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)

a=np.arange(1,13).reshape(3,4)
print(a)
b=np.arange(13,25).reshape(3,4)
print(b)
print("Column expanded: ")
print(np.concatenate((a,b),axis=0))
print("Row expanded: ")
print(np.concatenate((a,b),axis=1))
c=np.sum(a,axis=1)
print("Sum of rows:")
print(c)
d=np.concatenate((a,c.reshape(3,-1)),axis=1)
print("Concatenated A and C:")
print(d)
