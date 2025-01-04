class father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Father's Method")
    
class child(father):
    def display(self):
        print("Child's Method")
        
c=child('vishal10')
c.show()  # if there is no constructor in child it will go to father
c.display()
print(c.name)