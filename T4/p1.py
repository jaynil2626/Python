class father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Father's Method")
    
class child(father):
    def __init__(self,mark):
        self.mark=mark
    def display(self):
        print("Child's Method")
        
obj=child('vishal10')
obj.show()  #father's property can be accessed by child
obj.display()

# f=father('vishal10')
# f.show()  # you can't call method of child by father's object
# f.display()