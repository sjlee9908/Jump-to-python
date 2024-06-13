f = open('sample.txt', 'r')
a=f.readlines()
f.close()
a=list(map(int, a))

print(sum(a))
print(sum(a)/len(a))

f= open('result.txt', 'w')
b=sum(a)
f.write(str(b))
f.write('\n')
b=sum(a)/len(a)
f.write(str(b))


f.close()
