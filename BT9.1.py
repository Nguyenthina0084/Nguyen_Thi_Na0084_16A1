# In ra giá trị theo giấu của một số
import math
x = int ( input ( "Nhập số:" ))
if  x == 0 :
    print ( 0 )
elif  x > 0 :
    print ( 1 )
else :
    print ( - 1 )
print( math.sign ( x ))