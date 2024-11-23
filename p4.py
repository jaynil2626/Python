x=eval(input("Enter a list: "))
left_right=[]
right_left=[]
list=[]
result=[]
max=0

for i in range(0,len(x)):    
    if x[i] > max:
        max=x[i]
        left_right.append(max)
    else:
        left_right.append(max)

max=0
for i in range(len(x)-1,-1,-1):
    if x[i] > max:
        max=x[i]
        right_left.append(max)
    else:
        right_left.append(max)

right_left=right_left[::-1]

for i in range(0,len(x)):
    list.insert(i,min(right_left[i],left_right[i]))


for i in range(0,len(x)):
    result.insert(i,(list[i]-x[i]))

print(result)
print(sum(result))