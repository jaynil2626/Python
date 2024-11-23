d={'m':1000,'cm':900,'d':500,'cd':400,'c':100,'xc':90,'l':50,'xl':40,'x':10,'ix':9,'v':5,'iv':4,'i':1}
sum=0
rom=str(input("Enter a roman: "))
for i in range(0,len(rom)-1):
    if d[rom[i]] >= d[rom[i+1]]:
        sum+=d[rom[i]]
    elif d[rom[i]] < d[rom[i+1]]:
        sum-=d[rom[i]]
    else:
        print("Unexpected error occured ")

sum+=d[rom[len(rom)-1]]
print(sum)
count=0
n=int(input("Enter a number to convert into roman: "))
roman=""
for i,j in d.items():
    if n//j >0:
        count=n//j
        roman+=(i*count)
        n=n%j

print(roman)