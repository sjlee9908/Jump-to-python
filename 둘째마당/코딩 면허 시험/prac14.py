a=list(input())
b=list()
count=0
ex=a[0]

for i in a:
    if(ex != i):
        b.append(ex)
        b.append(count)
        ex=i
        count=1
    else:
        count+=1

b.append(ex)
b.append(count)

for i in b:
    print(i, end='')