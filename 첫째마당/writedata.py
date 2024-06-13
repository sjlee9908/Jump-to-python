f = open("C:/Users/Lee/OneDrive/공부/전공독서/프로그래밍 언어/점프 투 파이썬(이지스퍼블리싱, 박응용)/첫째마당/새파일.txt" , 'w')

for i in range(1,10):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()