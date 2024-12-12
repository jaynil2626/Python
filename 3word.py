# this program will return words from 'wordlist.txt' which contiain user entered string's character

f=open('wordlist.txt')
words=f.read().split()
user=input("Enter a string: ")
u={}
for i in user:
    u[i]=u.get(i,0)+1
for word in words:
    w={}
    flag=True
    for i in word:
        if i in u:
            w[i]=w.get(i,0)+1
    for i in u:
        if i in w:
            if u[i] <= w[i]:
                continue
        flag=False
    if flag==True:
        print(word) 
              