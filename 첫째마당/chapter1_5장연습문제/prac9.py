import sys

arg= sys.argv[1:]
res=0

for i in arg:
    res+=int(i)

print(res)