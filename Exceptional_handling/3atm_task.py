class ATM:
    blc=100000
    pinf=1234
    def __init__(self):
        pin=int(input("Enter your pin: "))
        if self.pinf!=pin:
            print("Invalid Pin, Enter Again !!!")
            self.__init__()
        else:
            self.menu()
            
    def withdraw(self,amt):
        if amt>self.blc:
            print("Insufficent Balance In ATM")
        else:
            self.blc=self.blc-amt
            print(f"Your current balance is {self.blc}")
            exit()
    
    def deposit(self):
        dep=int(input("Enter amount to deposit: "))
        self.blc=self.blc+dep
        print(f"Your current balance is {self.blc}")
        
    def display(self):
        print(f"Your balance is {self.blc} and pin is {self.pinf}")
        
    def chg_pin(self):
        pin=int(input("Enter your current pin: "))
        if self.pinf!=pin:
            print("Invalid Pin, Enter Again !!!")
            self.chg_pin()
        else:
            self.pinf=int(input("Enter new pin: "))
            print(f"Your pin has been successfully changed to {self.pinf}")
        
        

    def menu(self):
        while True:
            print("Enter 1 to withdraw amount: ")
            print("Enter 2 to deposit")
            print("Enter 3 to display Funds")
            print("Enter 4 to change pin")
            print("Enter 5 to Re-Login")
            print("Enter 6 to Exit")
            a=int(input())
            if a==1:
                amt=int(input("Enter amount to withdraw: "))
                self.withdraw(amt)
            elif a==2:
                self.deposit()
            elif a==3:
                self.display()
            elif a==4:
                self.chg_pin()
            elif a==5:
                c=ATM()
            elif a==6:
                exit()

b=ATM()