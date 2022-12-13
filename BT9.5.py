# Tính AA
import math
x=int(input())
n=int(input())
tinh_A= lambda x, n:math.pow((x**2+x+1),n)+math.pow((x**2-x+1),n)
print(tinh_A(x,n))