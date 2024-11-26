# L=['vishal','ravi','raj']
# L.sort(key=lambda x:x[-1])
# print(L)

# l=[[1,1,2,3,2],[4,3,2,1,3],[5,2,1,3,2],[3,2,1,4,5],[2,3,1,4,3]]
# d={}
# for i in l:
#     for j in i:
#         d[j]=d.get(j,0)+1
# print(d)
# l1=list(d.items())
# print(l1)
# l1.sort(key=lambda x:x[1],reverse=True)
# for i in range(0,2):
#     print(l1[i][0], l1[i][1])

# l=[-1,2,5,8,-3,9,-10]
#l.sort(key=lambda x:0 if x==0 else -1/x)
# print(l)

# l.sort(key=lambda x:x>0,reverse=True)
# print(l)
# l1=[]
# l2=[]
# for i in l:
#     if i>0:
#         l1.append(i)
#     else:
#         l2.append(i)

# l2.sort()
# print(l1,l2)
# l=l1+l2
# print(l)