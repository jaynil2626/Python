# class lj:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
    
#     def set(self,number):
#         print(number)

# s1=lj('V',10)
# print(s1.__dict__)
# s2=lj('H',9)
# print(s2.__dict__)
# s1.name='Vishal'
# print(s1.__dict__)

class vishal:
    movie='pushpa'
    def __init__(self,bud,rev):
        self.bud=bud
        self.rev=rev
    
    def set(self):
        print(self.movie)

o=vishal(10,20)
print(o.movie)
print(o.bud)
o.bud=50
o.movie='pushpa2'
print(o.movie)
print(o.bud)
print(o.__dict__)
print(vishal.movie)
vishal.movie='pushpa2'
print(vishal.movie)