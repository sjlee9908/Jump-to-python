import random

a=[]

while(len(a)!=6):
    b=random.randint(1,45)
    if b not in a:
        a.append(b)

print(a)