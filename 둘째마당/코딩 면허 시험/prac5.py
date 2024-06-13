n=int(input())

ex=0
exex=1
p=0

for x in range(2,n+1):
    p=ex+exex
    exex=ex
    ex=p

#if(n==1): p=1
print(p)