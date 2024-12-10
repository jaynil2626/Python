
# # cursor position f.tell()
# f=open('self.txt','a+')
# print(f.tell())
# f.write('hii')
# print(f.tell())
# f.seek(2) # position change f.seek()
# print(f.read())


# # with open (auto closed file as intendent over)
# with open('self.txt','r')as f:
#     print(f.read())
# with open('xyz.txt','r')as f:
#     print(f.read())
# print(f.closed)


# # print each line using for loop
# f=open('self.txt')
# for line in f:
#     print(line)
#     for word in line.split():
#         print(word)

# # print each character
# f=open('self.txt')
# r=f.read()
# for char in r:
#     print(char)


# # line and word count
# f=open('self.txt')
# print(len(f.readlines())) #line count
# f.close()
# f=open('self.txt')
# print(len(f.read().split())) # word count
# f.close()

# # character count
# f=open('self.txt')
# r=f.read()
# count=0
# for char in r:
#     count+=1
# print(count)



# # return line and column of mismatch character in both files
# f1=open('self.txt')
# f2=open('xyz.txt')
# l1=f1.readlines()
# l2=f2.readlines()
# flag=0
# for i in range(len(l1)):
#     if l1[i] != l2[i]:
#         for j in range(len(l1[i])):
#             if l1[i][j] != l2[i][j]:
#                 flag=1
#                 print("=========")
#                 print(l1[i][j],"!=",l2[i][j],"at")
#                 print("line: ",i+1)
#                 print("col:  ",j+1)

# if flag == 0:
#     print("no mismatch in both files")


# # comment words and write content in another file
# f1=open('self.txt')
# f2=open('xyz.txt','w')
# for line in f1:
#     if '#' not in line:
#         f2.write(line)
#     else:
#         if line.find('#') == 0:
#             continue
#         else:
#             a=line.find('#')
#             f2.write(line[0:a])
# f1.close()
# f2.close()


# # find 5 unique and longest words
# f=open('xyzz.txt')
# words=f.read().split()
# unique_words=set(words)
# unique_words_sorted=sorted(unique_words, key=lambda x: len(x), reverse=True)
# for i in range(5):
#     print(unique_words_sorted[i])

