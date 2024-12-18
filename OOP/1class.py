class lj:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        print(id(self))
    
    def set(number):
        print(number)

s1=lj('Vishal',10)
print(id(s1))
s1.set(30)
s2=lj('vha',9)
print(id(s2))