f= open("abc.txt", 'r')
a=f.readlines()
a.reverse()

f=open("abc.txt", 'w')

for i in a:
    i.strip()
    f.write(i)
    f.write('\n')

f.close()