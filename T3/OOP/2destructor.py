class vishal:
    def __init__(self):
        print("Class B3 is Creator")
    def __del__(self):
        print("Class B6 is Delete")
    def display(self):
        print("hii")
    
    
v=vishal()
v.display()
del v
v.display()
