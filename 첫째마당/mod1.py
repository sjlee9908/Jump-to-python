#mod1.py
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#mod1.py를 직접 실행할때는 print()문이 실행됨
#mod1.py를 import할 때는 실행되지 않음
if __name__ =="__main__":
    print(add(1,2))
    print(sub(4,2))