f = open('text.txt', 'r')
body = f.read()
f.close()

body = body.replace("java", "python")

f = open('text.txt', 'w')
f.write(body)
f.close()