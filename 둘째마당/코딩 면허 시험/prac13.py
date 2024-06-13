import copy

a=list(input())
i=0
while(i<len(a)-1):
    if(not a[i].isdigit()):
        i+=1
        continue
    ex=int(a[i])
    now=int(a[i+1])
    if(ex%2==1 and now%2==1): 
        a.insert(i+1, '-')
        i+=1
    elif(ex%2==0 and now%2==0): 
        a.insert(i+1, '*')
        i+=1
    else:
        i+=1

for i in a:
    print(i, end='')