# Tính A
import math
x = int(input("nhập x:"))
n = int(input("nhập n:"))
A = math.pow(math.pow(x,2)+x+1,n)+pow(pow(x,2)-x+1,n)
print("A=",A)