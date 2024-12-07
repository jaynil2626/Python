x=eval(input("Enter a list: "))

even=sum(x[0:len(x):2])
odd=sum(x[1:len(x):2])
y=x.copy()

if odd!=even:
        for i in range(0,len(x)):
            y.pop(i)
            even=sum(y[0::2])
            odd=sum(y[1::2])
            if odd==even:
                print("Your balanced list is ",y)
                break
            y=x.copy()
        else:
             print("this list can't be balanced")
             
            
else:
    print("list is already balanced")
    
