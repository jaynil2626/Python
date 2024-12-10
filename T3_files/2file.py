
# cursor position f.tell()
f=open('self.txt','a+')
print(f.tell())
f.write('hii')
print(f.tell())
f.seek(2) # position change f.seek()
print(f.read())