# Tính diện tích tam giác
import math
print("số đo 3 cạnh của tam giác là")
a = eval(input('số đo cạnh a ='))
b = eval(input('só đo cạnh b ='))
c = eval(input('số đo cạnh c ='))
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(" Diện tích tam giác là:", S)