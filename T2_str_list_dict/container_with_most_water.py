height=eval(input("enter of list "))
Area = 0

for left in range(0,len(height)):
    for right in range(left,len(height)):
        currentArea = min(height[left], height[right]) * (right - left)
        Area = max(Area, currentArea)
        
print(Area)
        
