# Xây dựng phương thức kiem_tra_so_nguyen_to(x)
def kiem_tra_so_nguyen_to(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
          count+=1

    if count>=2:
        return True
    else:
        return False
x=int(input("Nhập x:"))
print(kiem_tra_so_nguyen_to(x))