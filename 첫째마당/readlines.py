f = open("C:/Users/Lee/OneDrive/공부/전공독서/프로그래밍 언어/점프 투 파이썬(이지스퍼블리싱, 박응용)/첫째마당/새파일.txt" , 'r')

lines = f.readlines()
for line in lines:
    print(line)
f.close()
