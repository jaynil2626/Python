f=open('scores.txt')

# code to find average and scores of teams
l=[]
count=0
for line in f:
    detail=line.split()
    l.extend([int(detail[2]),int(detail[4])])
    count+=1
print(f"Avg points is {sum(l)/count}") 


# # code to find names of team 
# # (Extra block of code , not needed)
# name=[] 
# f.seek(0)
# for line in f:
#     detail=line.split()
#     name.extend([str(detail[1]),str(detail[3])])


# # code to find your input team's win-loss count
# f.seek(0)
# my_team=input("enter the name of the team:")
# loss=0
# won=0
# for line in f:
#     l=line.split()
#     if l[1] == my_team:
#         if int(l[2])>int(l[4]):
#             won += 1
#         else :
#             loss += 1
#     if l[3] == my_team:
#         if int(l[4])>int(l[2]):
#             won += 1
#         else:
#             loss += 1
# print(won,loss)


# find the teams that lost by 30 or more points the most times
f.seek(0)
list=[]
for line in f:
    l=line.split()
    if int(l[2]) > int(l[4]):
        diff= int(l[2])-int(l[4])
        if diff>=30:
            list.extend({l[3]})
    if int(l[4]) > int(l[2]):
        diff= int(l[4])-int(l[2])
        if diff>=30:
            list.extend({l[1]})
d={}
for i in list:
    d[i]=d.get(i,0)+1

k=[]
k.extend(d.items())
k.sort(key=lambda x:x[1], reverse=True)
print(k[0])

# another logic for: find the teams that lost by 30 or more points the most times
d={}
for line in f:
    l=line.split()
    if (int(l[2]))-int(l[4])>=30:
        d[l[3]]=d.get(l[3],0)+1
    if (int(l[4])-int(l[2]))>=30:
        d[l[1]]=d.get(l[1],0)+1
# print(d)
k=list(d.items())
k.sort(key=lambda x:x[1],reverse=True)
print(k[0][0],k[0][1])
    