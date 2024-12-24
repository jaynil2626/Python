# file=11 marks with no mcq ,,, module 5 marks all mcq,,, oop= mcq and 6 marks program or 9 mrks

# # File Opening
# self=open('self.txt','r')
# print(self)
# self.close() # Close File to free RAM

# # File Opening From Path (Other Directory)
# f=open('/workspaces/Python/T2_str_list_dict/abc.txt','r')
# print(f)
# f.close() # Close File

# # File Read
# self=open('self.txt','r')
# # f.write('Hello')  >>ERROR: File is only readable not writable
# x=self.read()
# print(x)
# y=self.read()
# print('>',y) # Blank Data because cursor is at end by reading x
# self.close()

# # Read And Write Mode (r+)
# self=open('self.txt','r+')
# x=self.read()
# print(x)
# self.write('123')
# y=self.read()
# print(">",y)
# self.close()


# # Over write file
# # you have to read first before writing to take cursor to end of content and after that do write
# self=open('self.txt','r+')
# self.write('v10') 
# self.close() #Hello > v10lo 

# # file not found error
# self=open('self1.txt','r+')
# self.close()

# # Write mode
# # if file does not exist in pwd it will create one
# xyz=open('xyz.txt','w')
# xyz.write('B6 is best') # if you open a file in write mode and write some data directly it will erase all data
# xyz.close()
# # print(f.read) # error: its in write mode


# #it will read nothing bcz the cursor will be at end after writing 
# xyz=open('xyz.txt','w+')
# xyz.write('B6 is best')
# print(xyz.read())
# xyz.close()


# # Append
# # if file does not exist in pwd it will create one
# xyz=open('xyz.txt','a')
# xyz.write('321') #B6 is best321 (it will add data at the end)
# # xyz.read() error:only write in append
# xyz.close()

# # a+ (read and write)
# xyz=open('xyz.txt','a+')
# print(xyz.read()) #cursor will be at end so blank due to append method
# xyz.write('321')
# xyz.close()

# self=open('self.txt', 'a+')
# print(self.name) # self.txt
# print(self.mode) # a+
# print(self.closed) # False
# print(self.readable()) #True
# print(self.writable()) #True
# self.close()


# # new line (\n)
# self=open('self.txt', 'w')
# self.write('12345 789')
# self.writelines(['a', 'b\n', 'c'])
# self.close() #output: 12345 789ab
# #                     c


# # imp for concept but out of syllabus
# self=open('self.txt', 'w')
# self.write('HI\n')
# self.writelines(['Hello\n','Welcome\n'])
# self.close()

# self=open('self.txt','r')
# print(self.readline()) # HI

# print(self.readlines()) # ['Hello\n', 'Welcome\n']

# print(self.read(2))
# print(self.read(4))
# print(self.read(7))
# print(self.read())
# self.close()


# self=open('self.txt', 'r')
# for i,j in enumerate(self, start=1):
#     print(i, '>', j)
# self.close()
# # 1 > HI
# # 2 > Hello
# # 3 > Welcome

# #print each words one by one
# self=open('self.txt','r')
# for i in self:
#     for j in i.split():
#         print(j)