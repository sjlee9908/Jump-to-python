a= input().split(' ')
bool_a=[]

for i in a:
    b=set(i)
    if(len(b)==len(i)==10):
        bool_a.append(True)
    else:
        bool_a.append(False)
    
for i in bool_a:
    print(i, end=' ')
        
