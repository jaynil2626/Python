# File Opening
self=open('self.txt','r')
print(self)
self.close() # Close File to free RAM

# File Opening From Path (Other Directory)
f=open('/workspaces/Python/T2_str_list_dict/abc.txt','r')
print(f)
f.close() # Close File