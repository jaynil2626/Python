class lj:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    
    def set(self,number):
        self.grade+=number
        print(self.grade)

s1=lj('vha',8)
s1.set(9)