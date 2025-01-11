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

a=np.array([[1,5,7],[2,5,1],[1,8,1]])
print(a)
print(np.where(a==1))
print(np.where(a==1 , 100,0))
b=np.array([[30,20,40],[50,60,70],[10,30,50]])
print(b)
print(np.where(b>50,1,np.where(b>30,2,3)))
