x=str(input("Enter a message: "))
y=int(input("Enter key: "))
new=" "
for i in range(0,y):
    print(x[i::y], end="")

