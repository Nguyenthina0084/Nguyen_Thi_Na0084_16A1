# Tìm BCNN(A,B)
a=int(input("a = "))
b=int(input("b = "))
x,y=a,b
while x!=y:
    if x>y:
        x=x-y
    else:
        y=y-x
print("Bội chung nhỏ nhất của",a, "và", b,"là: ",a*b/x)