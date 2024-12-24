def find(a,b):
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return i

def rfind(a,b):
    ans='the string is not available'
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            ans=i
    return ans
