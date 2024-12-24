# # 1) Program
# f=open('mbox-short.txt')
# count=0
# for line in f:
#     if not line.startswith('From '):
#         continue
#     print(line.split()[1])
#     count+=1
# print(count)


# # 2) Program
# # find max duplicate counts
# f=open('mbox-short.txt')
# l=[]
# count=0
# for line in f:
#     if not line.startswith('From '):
#         continue
#     print(line.split()[1])
#     l.append(line.split()[1])
#     count+=1
# print(count)
# d={}
# for i in l:
#     d[i]=d.get(i,0)+1
# # print(d)
# k=list(d.items())
# k.sort(key=lambda x:x[1],reverse=True)
# print(k)


# # 3) Program
# f=open('mbox-short.txt')
# l=[]
# for line in f:
#     if not line.startswith('From '):
#         continue
#     l.append(line.split()[5].split(':')[0])
# l.sort(reverse=True)
# print(l)
# d={}
# for i in l:
#     d[i]=d.get(i,0)+1

# k=list(d.items())
# k.sort(key=lambda x:x[1])
# print(k)


# # 4) Program
# f=open('mbox-short.txt')
# l=[]
# sm,count=0.0,0
# for line in f:
#     if not line.startswith('X-DSPAM-Confidence: '):
#         continue
#     print(line.split()[1])
#     count+=1
#     sm+=float(line.split()[1])
# print("count: ",count)
# print("Average: ",sm/count)


# # 5) Program
# f=open('logfile.txt')
# for line in f:
#     if int(line.split()[2].split(':')[0]) - int(line.split()[1].split(':')[0]) >1 :
#         print(line)
#     elif int(line.split()[2].split(':')[0]) - int(line.split()[1].split(':')[0]) ==1 :
#         if int(line.split()[2].split(':')[0]) > int(line.split()[1].split(':')[0]) :
#             print(line)


# # 6) Program
# f=open('namelist.txt')
# x=str(input("Enter a short name: "))
# for line in f:
#     l=line.split()
#     if len(x)==2:
#         if x[0] == l[0][0] and x[1] == l[-1][0]:
#             print(" ".join(l))
#     if len(x) == 3 and len(l) == 3:
#         if x[0] == l[0][0] and x[1] == l[1][0] and x[2] == l[2][0]:
#             print(" ".join(l))
