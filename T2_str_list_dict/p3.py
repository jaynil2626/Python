x=eval(input("Enter a list: "))
even=()
odd=()


for i in range(0,len(x),1):
    if x[i] %2 ==0:
        even+=tuple([x[i]])
    else:
        odd+=tuple([x[i]])

emax=x[0]
omax=x[0]
emin=x[0]
omin=x[0]

for i in range(0,len(even),1):
    if even[i]>emax:
        emax=even[i]
    elif even[i]<emin:
        emin=even[i]


for i in range(0,len(odd),1):
    if odd[i]>omax:
        omax=odd[i]
    elif odd[i]<omin:
        omin=odd[i]

print(f"even max {emax} and even min {emin}")
print(f"odd max {omax} and odd min {omin}")