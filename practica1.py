tem=""
x=0
a = 3
b = 4
while x<4:
    x+=1
    tem+=str(a)+("+")

print(tem[:-1] + "=" + str(int(a)*int(b)))