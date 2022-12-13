# Xây dựng chương trình tinh_S(n,x)
import math
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
tinh_S= lambda x, n: math.pow(math.pow(x,2)+1,n)
print(tinh_S(x,n))